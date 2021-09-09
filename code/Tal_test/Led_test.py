#!/usr/bin/env python
# coding: utf-8



import sacn
import time
import math


sender = sacn.sACNsender()  # provide an IP-Address to bind to if you are using Windows and want to use multicast
sender.start()  # start the sending thread
sender.activate_output(1)  # start sending out data in the 1st universe
sender[1].multicast = True  # set multicast to True
# sender[1].destination = "192.168.1.20"  # or provide unicast information.
# Keep in mind that if multicast is on, unicast is not used

for j in range (10):
    for i in range (360):
        print("i: %s " % i)
        z = int((1+(math.sin(math.radians(i)))) *127)
        y = int((1+(math.sin(math.radians(i+120)))) *127)
        x = int((1+(math.sin(math.radians(i+240)))) *127)
        print(z)
        sender[1].dmx_data = (x,0,0,y,0,0,z,0,0)
        time.sleep(0.01)

sender.manual_flush = True # turning off the automatic sending of packets
sender[1].dmx_data = (0, 0, 0, 0, 0, 0, 0, 0, 0)  # blank out
sender.flush()
sender.manual_flush = False # keep manual flush off as long as possible, because if it is on, the automatic
# sending of packets is turned off and that is not recommended

sender[1].dmx_data = (0, 128, 0, 128, 0, 0, 0, 0, 128)  # some DMX data
time.sleep(1)  # send the data for 1 seconds
sender[1].dmx_data = (128, 0, 0, 0, 0, 128, 0, 128, 0)  # some DMX data
time.sleep(1)  # send the data for 1 seconds
sender[1].dmx_data = (0, 0, 128,  0, 128, 0, 128, 0, 0 )  # some DMX data
time.sleep(1)  # send the data for 1 seconds

sender.manual_flush = True # turning off the automatic sending of packets
sender[1].dmx_data = (0, 0, 0, 0, 0, 0, 0, 0, 0)  # blank out
sender.flush()
# time.sleep(0.1)
sender.manual_flush = False # keep manual flush off as long as possible, because if it is on, the automatic
# sending of packets is turned off and that is not recommended
sender.stop()  # do not forget to stop the sender
