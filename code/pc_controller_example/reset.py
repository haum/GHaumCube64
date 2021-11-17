#! /usr/bin/env python
# -*- coding:utf8 -*-

import time
import threading

from controller import TalController

C = TalController(Ntal=64, Nled=3, source_name="HAUM Resetter")
C.fill()
C.stop()
for thread in threading.enumerate():
    if thread != threading.current_thread(): thread.join()
