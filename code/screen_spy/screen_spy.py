#!/usr/bin/env python3

import json
import os
import platform
import signal
import threading
import time

import pyglet
import sacn

lock = threading.Lock()

values = [0] * 576
oldvalues = [-1] * 576

stats = {}
stats_filename = os.path.dirname(os.path.realpath(__file__))+'/stats.json'
if os.path.isfile(stats_filename):
    with open(stats_filename, 'r') as f:
        stats = json.load(f)
if not 'history' in stats: stats['history'] = []

receiver = sacn.sACNreceiver()
receiver.start()

window = pyglet.window.Window(width=1920, height=1080, caption='24HC21 spy screen')
if platform.node() == 'raspberrypi':
    window.set_fullscreen()
background = pyglet.resource.image('bg.png')
batch1 = pyglet.graphics.Batch()
batch2 = pyglet.graphics.Batch()

w, h = 35, 16
rects = []
labels = []
for i in range(576):
    x = 50+(i%9)*w
    y = window.height-26-(i//9)*h
    rect = pyglet.shapes.Rectangle(x-w/2+1, y-h+1, w-2, h-2, color=(255, 200, 0), batch=batch1)
    rect.opacity = 0
    rects.append(rect)
    labels.append(pyglet.text.Label(font_name='Monospace', font_size=10, x=x, y=y, anchor_x='center', anchor_y='top', batch=batch2))

lbl_log = pyglet.text.Label(font_name='Monospace', color=(255, 255, 255, 64), font_size=20, x=380, width=window.width-380, y=30, anchor_x='left', anchor_y='bottom', multiline=True, batch=batch1)

logupdate = 0
def update(dt):
    global logupdate, oldvalues

    do = dt * 64
    for r in rects:
        if r.opacity > 0:
            r.opacity = 0 if r.opacity < do else r.opacity - do

    updated = False
    for l, r, v, ov in zip(labels, rects, values, oldvalues):
        if v != ov:
            l.text = str(v)
            r.opacity = 128
            updated = True
    if updated:
        oldvalues = values.copy()

    logupdate += dt
    if logupdate > 0.5:
        logupdate = 0
        logs = []
        for l in stats['history'][-32:]:
            logs.append(
                time.strftime('%H:%M:%S', time.localtime(l['firstTime'])) + ' > ' +
                time.strftime('%H:%M:%S', time.localtime(l['lastTime'])) + '   ' +
                l['sourceName']
            )
        lbl_log.text = '\n'.join(logs)

@window.event
def on_draw():
    with lock:
        window.clear()
        background.blit(0, 0)
        batch1.draw()
        batch2.draw()

def sacn_received(universe, packet):
    with lock:
        if universe == 1:
            values[:510] = packet.dmxData[:510]
        else:
            values[-66:] = packet.dmxData[:66]

        if len(stats['history']) == 0 or stats['history'][-1]['sourceName'] != packet.sourceName:
            stats['history'].append({
                'sourceName': packet.sourceName,
                'firstTime': time.time(),
                'lastTime': time.time(),
            })
        else:
            stats['history'][-1]['lastTime'] = time.time()

@receiver.listen_on('universe', universe=1)
def callback(packet):
    sacn_received(1, packet)

@receiver.listen_on('universe', universe=2)
def callback(packet):
    sacn_received(2, packet)

def signal_USR1_handler(signum, frame):
    with lock:
        names = set(l['sourceName'] for l in stats['history'])
        for n in names:
            d = sum(l['lastTime'] - l['firstTime'] for l in stats['history'] if l['sourceName'] == n)
            print(f'\033[96m{d:10.1f} \033[93m{n}\033[0m')

try:
    signal.signal(signal.SIGUSR1, signal_USR1_handler)
    receiver.join_multicast(1)
    receiver.join_multicast(2)
    pyglet.clock.schedule_interval(update, 1/30.0)
    pyglet.app.run()
except KeyboardInterrupt:
    pass

with open(stats_filename, 'w') as f:
    json.dump(stats, f)

receiver.stop()
