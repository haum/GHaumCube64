#!/usr/bin/env python3

import itertools
import pyglet
import sacn
from math import radians

window = pyglet.window.Window(width=800, height=800)
batch = pyglet.graphics.Batch()
pyglet.gl.glClearColor(0.15,0.2,0.2,1)
window.view = window.view.translate((400, 0, 0))
window.view = window.view.rotate(radians(45), (0, 0, 1))

def make_polygons(x, y, w_small, w_large, h):
    polys = []

    l1 = 0.015
    l2 = (1 - 3*l1) / 4
    partsx = (0, l2, l2+l1, l2+l1+l2, 1-l2-l1-l2, 1-l2-l1,  1-l2, 1)

    l1 = 0.03
    l2 = (1 - 3*l1) / 4
    partsy = (0, l2, l2+l1, l2+l1+l2, 1-l2-l1-l2, 1-l2-l1,  1-l2, 1)

    for xc0, yc0 in itertools.product(range(4), range(4)):
        xc, yc = 3-xc0, 3-yc0
        cw1 = w_small+(w_large-w_small)*(1-partsy[2*yc])
        cw2 = w_small+(w_large-w_small)*(1-partsy[2*yc+1])
        cc = [
            (x+partsx[2*xc]*cw1+(w_large-cw1)/2, y+partsy[2*yc]*h),
            (x+partsx[2*xc+1]*cw1+(w_large-cw1)/2, y+partsy[2*yc]*h),
            (x+partsx[2*xc+1]*cw2+(w_large-cw2)/2, y+partsy[2*yc+1]*h),
            (x+partsx[2*xc]*cw2+(w_large-cw2)/2, y+partsy[2*yc+1]*h),
        ]
        s = pyglet.shapes.Polygon(*cc, color=(0, 0, 0), batch=batch)
        polys.append(s)
    return polys

cases = []
sqrt2 = 1.414213562
for i0 in range(4):
    i = 3-i0
    cases.extend(make_polygons(30, 90+180/sqrt2*i, 400/sqrt2, 700/sqrt2, 160/sqrt2))

positions = [1,35,38,40,15,25,33,32,18,23,28,31,20,21,22,30,55,45,43,41,5,2,36,39,13,16,26,34,12,19,24,29,58,53,48,42,63,56,46,44,8,6,3,37,11,14,17,27,60,52,51,50,61,59,54,49,62,64,57,47,10,9,7,4]
cases = [x for _,x in sorted(zip(positions, cases))]

@window.event
def on_draw():
    window.clear()
    batch.draw()

def on_update(dt):
    pass # Empty function is needed, otherwise pyglet wont update

pyglet.clock.schedule_interval(on_update, 1/30)

receiver = sacn.sACNreceiver()
receiver.start()
receiver.join_multicast(1)
receiver.join_multicast(2)

@receiver.listen_on('universe', universe=1)
def sacn_received_univ1(packet):
    for i,c in enumerate(cases[:56]):
        c.color = packet.dmxData[9*i:9*i+3]
        pyglet.clock.schedule_once(lambda x: x, 0)

@receiver.listen_on('universe', universe=2)
def sacn_received_univ2(packet):
    for i,c in enumerate(cases[56:]):
        c.color = packet.dmxData[9*i:9*i+3]

try:
    pyglet.app.run()
except KeyboardInterrupt:
    pass

receiver.stop()
