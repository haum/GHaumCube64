#!/usr/bin/env python3

import numpy as np
import sacn

placement = np.array([
    1, 35, 38, 40,   15, 25, 33, 32,  18, 23, 28, 31,  20, 21, 22, 30,
    55, 45, 43, 41,  5, 2, 36, 39,    13, 16, 26, 34,  12, 19, 24, 29,
    58, 53, 48, 42,  63, 56, 46, 44,  8, 6, 3, 37,     11, 14, 17, 27,
    60, 52, 51, 50,  61, 59, 54, 49,  62, 64, 57, 47,  10, 9, 7, 4
]).reshape(4, 4, 4)


def coord_3d_to_linear(x, y, z):
    assert x >= 0 and x <= 3 and y >= 0 and y <= 3 and z >= 0 and z <= 3
    return int(placement[x, y, z]) - 1


def coord_linear_to_3d(n):
    assert n >= 0 and n <= 63
    return tuple(map(lambda x: int(x[0]), np.where(placement == n)))


class LedIndexing:
    def __init__(self, controller):
        self.controller = controller

    def __setitem__(self, k, v):
        self.controller.chans[k*3:(k+1)*3] = v


class TalIndexing:
    def __init__(self, controller):
        self.controller = controller

    def __setitem__(self, k, v):
        for i in range(3):
            self.controller.leds[k*3+i] = v


class XYZIndexing:
    def __init__(self, controller):
        self.controller = controller

    def __setitem__(self, k, v):
        self.controller.tals[coord_3d_to_linear(*k)] = v


class CubeSacnController:
    def __init__(self, name='CubeSacnController', **kw):
        self.fill()

        self.sender = sacn.sACNsender(source_name=name, **kw)
        self.sender.start()
        self.sender.activate_output(1)
        self.sender.activate_output(2)
        self.sender[1].multicast = True
        self.sender[2].multicast = True
        self.sender.manual_flush = True

        self.leds = LedIndexing(self)
        self.tals = TalIndexing(self)
        self.xyz = XYZIndexing(self)

    def fill(self, val=[0]*3):
        self.chans = val*64*3

    def stop(self):
        self.fill()
        self.blit()
        self.sender.stop()

    def blit(self):
        self.sender[1].dmx_data = self.chans[:510]
        self.sender[2].dmx_data = self.chans[510:]
        self.sender.flush()
