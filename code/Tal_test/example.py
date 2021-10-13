#! /usr/bin/env python
# -*- coding:utf8 -*-

from controller import TalController


C = TalController(Ntal=24, Nled=3)

# all to white
C.fill([0xff, 0xff, 0xff])

# or
C.fill([255, 255, 255])

# light up the tenth tål in red
C.only(9, [255, 0, 0])

# Start a blue chaser with a 0.2s delay
C.chaser([0, 0, 255], 0.2)

# Now empty The Tål and light up number 1 in red, 2, in green and 3 in blue
C.fill()
C[0] = [255, 0, 0]
C[1] = [0, 255, 0]
C[2] = [0, 0, 255]
C.blit()

# and stop the thingy
C.stop()

