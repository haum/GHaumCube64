#! /usr/bin/env python
# -*- coding:utf8 -*-

import time
from controller import TalController
from plasma_gradient import plasma_gradient

C = TalController(Ntal=64, Nled=3, source_name='HAUM tal position example')

try:
    for i in range(64):
        C[i] = plasma_gradient(i/64.0)
    C.blit()

    while True:
        for i in range(64):
            C[i] = [128, 255, 128]
            C.blit()
            time.sleep(0.4)
            C[i] = plasma_gradient(i/64.0)

except KeyboardInterrupt:
    pass

C.stop()
