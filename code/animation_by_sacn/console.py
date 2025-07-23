#!/usr/bin/env python3

import sys
import select
from color_animation import period_decode as pdec


def parseInt(line: str):
    try:
        return int(line)
    except ValueError:
        return 0


def parseFloat(line: str):
    try:
        return float(line)
    except ValueError:
        return 0


def parseColor(line: str):
    a = line.split(' ')
    if len(a) != 3:
        return (0, 0, 0)
    return tuple(map(parseInt, a))


class Console:
    def __init__(self, data):
        self.data = data
        self.change_input(self.input_menu)

    def change_input(self, fct):
        self.input = fct
        self.input(None)

    def input_menu(self, line: str):
        if line is None:
            d = self.data[0]
            print(f'c1: {d[0:3]} c2: {d[3:6]} fx: {d[6]} p:{pdec(d[7])} f:{d[8]}')
            print('1. Color 1')
            print('2. Color 2')
            print('3. Fx')
            print('4. Fx--')
            print('5. Fx++')
            print('6. Period')
            print('7. Fading')
            return
        n = parseInt(line)
        if n == 1:
            self.change_input(self.input_color1)
        elif n == 2:
            self.change_input(self.input_color2)
        elif n == 3:
            self.change_input(self.input_fx)
        elif n == 4:
            self.data[0][6] -= 1
            self.input_menu(None)
        elif n == 5:
            self.data[0][6] += 1
            self.input_menu(None)
        elif n == 6:
            self.change_input(self.input_period)
        elif n == 7:
            self.change_input(self.input_fading)
        else:
            print('Incorrect input')
            self.input_menu(None)

    def input_color1(self, line: str):
        if line is None:
            print('Color?')
            return
        self.data[0][0:3] = parseColor(line)
        self.change_input(self.input_menu)

    def input_color2(self, line: str):
        if line is None:
            print('Color?')
            return
        self.data[0][3:6] = parseColor(line)
        self.change_input(self.input_menu)

    def input_fx(self, line: str):
        if line is None:
            print('Fx?')
            return
        self.data[0][6] = parseInt(line)
        self.change_input(self.input_menu)

    def input_period(self, line: str):
        if line is None:
            print('Period? (s)')
            return
        self.data[0][7] = min(max(0, int(parseFloat(line)*10)), 255)
        self.change_input(self.input_menu)

    def input_fading(self, line: str):
        if line is None:
            print('Fading?')
            return
        self.data[0][8] = min(max(0, parseInt(line)), 255)
        self.change_input(self.input_menu)

    def process(self, timeout=0):
        if sys.stdin.isatty():
            r, _, _ = select.select([sys.stdin], [], [], timeout)
            if r:
                self.input(sys.stdin.readline())


if __name__ == '__main__':
    import sacn

    sender = sacn.sACNsender(source_name='console_sacn')
    sender.start()
    sender.activate_output(3)
    sender[3].multicast = True
    sender.manual_flush = True

    data = [[255, 0, 0, 0, 0, 0, 2, 0, 0]]
    console = Console(data)

    try:
        while True:
            console.process(1)
            sender[3].dmx_data = data[0]
            sender.flush()
    except KeyboardInterrupt:
        sender.stop()
