#! /usr/bin/env python
# -*- coding:utf8 -*-

import sacn
import time

class WS2812_led:

    def __init__(self, Nbled = 128, destip = None ):

        """
        Parameters
        ----------

        Nbled: int
            Number of connected ws2812_led

        destip:
            destination IP in unicast sender

        """
        nb_univers = int (Nbled/170)
        self.nb_univers = nb_univers

        # provide IP-Address to bind to if you are using Windows and want to use multicast
        self.sender = sacn.sACNsender(source_name = "WS2812_SACN by HAUM.ORG")
        self.sender.start()  # start the sending thread
        for un in range(nb_univers):
            self.sender.activate_output(un+1)  # start sending out data in the universe
            if destip != None :
                self.sender[un+1].destination = destip
            else:
                self.sender[un+1].multicast = True
        self.Nbled = Nbled

    def used_univers(self):
        return self.nb_univers+1

class TalController:
    """Controller for The Tål over sACN/E1.31

    The __setitem__, __getitem__ and __delitem__ methods are implemented
    and allow to address a given tål by simply slicing this controller and assigning a
    color. The ``del controller[k]`` is a short-hand for ``controller[k] = [0, 0, 0]``.
    Remember to call ``controller.blit()`` if your using slicing interface.

    Parameters
    ----------

    Ntal: int
        Number of Tåler
    Nled: int
        Number of LED per Tål
    """

    def __init__(self, Ntal=64, Nled=3):
        """
        Parameters
        ----------

        Ntal: int
            Number of connected Tål

        Nled: int
            Number of LEDs per tål
        """

        # provide IP-Address to bind to if you are using Windows and want to use multicast
        self.sender = sacn.sACNsender(source_name = "WS2812_SACN by HAUM.ORG")
        self.sender.start()  # start the sending thread
        self.sender.activate_output(1)  # start sending out data in the 1st universe
        self.sender[1].multicast = True  # set multicast to True
        # self.sender[1].destination = destip  # or provide unicast information.
        # Keep in mind that if multicast is on, unicast is not used

        self.Ntal = Ntal
        self.Nled = Nled

        self._taler = None
        self.fill()
        self.blit()

    def stop(self, reset=True):
        """Stop the sender"""
        if reset:
            self.fill()
        self.sender.stop()

    def blit(self):
        """Blit the stored state of LED to The Tål"""
        self.sender[1].dmx_data = sum([self._taler[_]*self.Nled for _ in range(self.Ntal)], [])

    def fill(self, color=[0,0,0]):
        """Fill the whole Tål with a given color (default: black)

        Parameters
        ----------

        color: 3-list of bytes
            Color specification (3 bytes)
        """
        self._taler = {_: color for _ in range(self.Ntal)}
        self.blit()

    def only(self, talid, color):
        """Light only one of the tåler with a given color

        Parameters
        ----------

        talid: int
            Index of the tål to light up (<Ntal from __init__)
        color: 3-list of bytes
            Color specification (3 bytes)
        """
        if talid >= self.Ntal:
            raise ValueError('Invalid Tål id {}'.format(talid))

        self.fill()
        self._taler[talid] = color
        self.blit()

    def chaser(self, color=[255, 255, 255], delay=0.5):
        """Play a chaser on all the tåler with a given delay

        Parameters
        ----------

        color: 3-list of bytes
            Color specification (3 bytes)
        delay: float
            Delay between 2 light ups
        """
        self.fill()
        for idx in range(self.Ntal):
            self.only(idx, color)
            time.sleep(delay)

    def __getitem__(self, k):
        return self._taler[k]

    def __setitem__(self, k, v):
        self._taler[k] = v

    def __delitem__(self, k):
        self._taler[k] = [0, 0, 0]
