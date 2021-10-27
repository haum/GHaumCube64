#! /usr/bin/env python
# -*- coding:utf8 -*-

import time
import math

import sacn


class WS2812_led:

    def __init__(self, Nbled=128, destip=None):

        """
        Parameters
        ----------

        Nbled: int
            Number of connected ws2812_led

        destip:
            destination IP in unicast sender

        """

        self.Nbled_by_universe = 170
        self.nb_universes = math.ceil(Nbled/self.Nbled_by_universe)

        # provide IP-Address to bind to if you are using Windows and want to use multicast
        self.sender = sacn.sACNsender(source_name = "WS2812_SACN by HAUM.ORG")
        self.sender.start()  # start the sending thread
        for un in range(self.nb_universes):
            self.sender.activate_output(un+1)  # start sending out data in the universe
            if destip != None :
                self.sender[un+1].destination = destip
            else:
                self.sender[un+1].multicast = True
        self.Nbled = Nbled
        self._leds = None
        self.fill()

    def fill(self, color=[0, 0, 0], blit=False):
        self._leds = {iu:
            {il: color for il in range(self.Nbled_by_universe)}
        for iu in range(1, 1+self.nb_universes)}
        if blit:
            self.blit()

    def __blit_universe(self, universe):
        self.sender[universe].dmx_data = sum([self._leds[universe][i] for i in range(self.Nbled_by_universe)], [])

    def blit(self, universe=-1):
        if universe == -1:
            list_universes = range(1, 1+self.nb_universes)
        else:
            if type(universe) in [list, tuple]:
                list_universes = universe
            elif type(universe) == int:
                list_universes = [universe]
        for u in list_universes:
            self.__blit_universe(u)

    def dmx(self, idx, color, blit=False):
        id_universe = 1 + math.floor(idx/self.Nbled_by_universe)
        id_led = idx - (id_universe - 1)*self.Nbled_by_universe
        self._leds[id_universe][id_led] = color
        if blit:
            self.blit(id_universe)

    def stop(self, reset=True):
        """Stop the sender"""
        if reset:
            self.fill(blit=True)
        self.sender.stop()

    def __getitem__(self, ledid):
        return self._leds[ledid]

    def __setitem__(self, ledid, color):
        self._leds[ledid] = color

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

        self.Ntal = Ntal
        self.Nled = Nled

        self.leds = WS2812_led(Nbled=Ntal*Nled)

        print(Ntal*Nled)
        self.leds.fill(blit=True)

    def stop(self, reset=True):
        """Stop the sender"""
        self.leds.stop(reset)

    def blit(self):
        """Blit the stored state of LED to The Tål"""
        self.leds.blit()

    def fill(self, color=[0,0,0]):
        """Fill the whole Tål with a given color (default: black)

        Parameters
        ----------

        color: 3-list of bytes
            Color specification (3 bytes)
        """
        self.leds.fill(color, blit=True)

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

        self.leds.fill()
        self[talid] = color
        self.leds.blit()

    def chaser(self, color=[255, 255, 255], delay=0.5):
        """Play a chaser on all the tåler with a given delay

        Parameters
        ----------

        color: 3-list of bytes
            Color specification (3 bytes)
        delay: float
            Delay between 2 light ups
        """
        for idx in range(self.Ntal):
            self.only(idx, color)
            time.sleep(delay)

    def __getitem__(self, talid):
        return self.leds[talid*self.Nled]

    def __setitem__(self, talid, color):
        for i in range(talid, talid+self.Nled):
            self.leds.dmx(i, color)

    def __delitem__(self, k):
        self[k] = [0, 0, 0]
