#! /usr/bin/env python
# -*- coding:utf8 -*-

import time

from controller import TalController

C = TalController(Ntal=64, Nled=3, source_name="HAUM Resetter")
C.fill()
C.stop()
