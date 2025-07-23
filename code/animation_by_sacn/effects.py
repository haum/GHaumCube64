#!/usr/bin/env python3

import sys
import itertools
import random


def all_effects(cube_animator):
    return [
        sys.modules[__name__].__getattribute__(e)(cube_animator)
        for e in dir(sys.modules[__name__])
        if e.startswith('Effect_')
    ]


def helper_inout(o):
    for i in range(4):
        o((i, i, i), 5)
    for i in range(3):
        o((1+i, i, i), 4)
        o((i, 1+i, i), 4)
        o((i, i, 1+i), 4)
        o((i, 1+i, 1+i), 4)
        o((1+i, i, 1+i), 4)
        o((1+i, 1+i, i), 4)
    for i in range(2):
        o((i, 2+i, 1+i), 3)
        o((i, 1+i, 2+i), 3)
        o((2+i, i, 1+i), 3)
        o((1+i, i, 2+i), 3)
        o((2+i, 1+i, i), 3)
        o((1+i, 2+i, i), 3)
    for i in range(2):
        o((2+i, i, i), 2)
        o((i, 2+i, i), 2)
        o((i, i, 2+i), 2)
        o((i, 2+i, 2+i), 2)
        o((2+i, i, 2+i), 2)
        o((2+i, 2+i, i), 2)
    for i in range(4):
        o((3, i, 0), 1)
        o((3, 0, i), 1)
        o((i, 3, 0), 1)
        o((0, 3, i), 1)
        o((i, 0, 3), 1)
        o((0, i, 3), 1)


def helper_outin(o):
    for i in range(4):
        o((i, i, i), 1)
    for i in range(3):
        o((1+i, i, i), 2)
        o((i, 1+i, i), 2)
        o((i, i, 1+i), 2)
        o((i, 1+i, 1+i), 2)
        o((1+i, i, 1+i), 2)
        o((1+i, 1+i, i), 2)
    for i in range(2):
        o((i, 2+i, 1+i), 3)
        o((i, 1+i, 2+i), 3)
        o((2+i, i, 1+i), 3)
        o((1+i, i, 2+i), 3)
        o((2+i, 1+i, i), 3)
        o((1+i, 2+i, i), 3)
    for i in range(2):
        o((2+i, i, i), 4)
        o((i, 2+i, i), 4)
        o((i, i, 2+i), 4)
        o((i, 2+i, 2+i), 4)
        o((2+i, i, 2+i), 4)
        o((2+i, 2+i, i), 4)
    for i in range(4):
        o((3, i, 0), 5)
        o((3, 0, i), 5)
        o((i, 3, 0), 5)
        o((0, 3, i), 5)
        o((i, 0, 3), 5)
        o((0, i, 3), 5)


def helper_edges(o):
    for i in range(4):
        o((i, 0, 0), 10-i)
        o((0, i, 0), 10-i)
        o((0, 0, i), 10-i)
    for i in range(2):
        o((3, i+1, 0), 6-i)
        o((3, 0, i+1), 6-i)
        o((i+1, 3, 0), 6-i)
        o((0, 3, i+1), 6-i)
        o((i+1, 0, 3), 6-i)
        o((0, i+1, 3), 6-i)
    for i in range(4):
        o((i, 3, 3), 4-i)
        o((3, i, 3), 4-i)
        o((3, 3, i), 4-i)


class Effect:
    def __init__(self, cube_animator):
        self.ca = cube_animator

    def onStart(self): pass
    def onColor1Changed(self): pass
    def onColor2Changed(self): pass
    def onColorsChanged(self): pass
    def onPeriodChanged(self): pass
    def onAnimate(self, dt): pass
    def onStop(self): pass


class Effect_01_Fill(Effect):
    def onStart(self):
        for i in range(64):
            self.ca[i].set_colors(1, 1)


class Effect_02_Wipe(Effect):
    def onStart(self):
        for i in range(64):
            self.ca[i].set_colors()
            self.ca[i].set_duty_cycle(1/2)
            self.ca[i].set_phase_percent(1-i/128)


class Effect_03_Chaser(Effect):
    def onStart(self):
        for i in range(64):
            self.ca[i].set_colors()
            self.ca[i].set_duty_cycle(1/64)
            self.ca[i].set_phase_percent(1-i/64)


class Effect_04_Flicker(Effect):
    def update(self):
        s = random.sample(list(range(64)), 14)
        s1, s2 = s[:7], s[7:]
        for i in range(64):
            if i in s1:
                self.ca[i].set_colors()
                self.ca[i].set_duty_cycle(1/10)
                self.ca[i].set_phase_percent(0)
            elif i in s2:
                self.ca[i].set_colors()
                self.ca[i].set_duty_cycle(1/10)
                self.ca[i].set_phase_percent(1/3)
            else:
                self.ca[i].set_colors(2, 2)

    def onStart(self):
        self.progress_percent = 0
        self.update()

    def onAnimate(self, dt):
        self.progress_percent += 4 * dt / self.ca.period
        if self.progress_percent > 1:
            self.update()
            self.progress_percent = 0


class HelperEffect_ChaserFace(Effect):
    def update(self, v):
        for xyz in itertools.product(range(4), repeat=3):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/4)
            self.ca[xyz].set_phase_percent((4-xyz[v])/4)


class Effect_05_ChaserFaceX(HelperEffect_ChaserFace):
    def onStart(self): self.update(0)


class Effect_06_ChaserFaceY(HelperEffect_ChaserFace):
    def onStart(self): self.update(1)


class Effect_07_ChaserFaceZ(HelperEffect_ChaserFace):
    def onStart(self): self.update(2)


class Effect_08_ChaserFaceXYZ(HelperEffect_ChaserFace):
    def onStart(self):
        self.progress_percent = 0
        self.pos = 0
        self.update(self.pos)

    def onAnimate(self, dt):
        self.progress_percent += dt / self.ca.period
        if self.progress_percent >= 1:
            self.pos = (self.pos + 1) % 3
            self.update(self.pos)
            self.progress_percent = 0


class Effect_09_ChaserVertical(Effect):
    def onStart(self):
        for xyz in itertools.product(range(4), repeat=3):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/10)
            self.ca[xyz].set_phase_percent(1-sum(xyz)/10)


class Effect_10_ChaserInOut(Effect):
    def onStart(self):
        def o(xyz, phase):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/5)
            self.ca[xyz].set_phase_percent(phase/5)
        helper_inout(o)


class Effect_11_ChaserOutIn(Effect):
    def onStart(self):
        def o(xyz, phase):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/5)
            self.ca[xyz].set_phase_percent(phase/5)
        helper_outin(o)


class Effect_12_ChaserEdges(Effect):
    def onStart(self):
        def o(xyz, phase):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/10)
            self.ca[xyz].set_phase_percent(phase/10)
        for i in range(64):
            self.ca[i].set_colors(2, 2)
        helper_edges(o)


class HelperEffect_WipeFace(Effect):
    def update(self, v):
        for xyz in itertools.product(range(4), repeat=3):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/2)
            self.ca[xyz].set_phase_percent((8-xyz[v])/8)


class Effect_13_WipeFaceX(HelperEffect_WipeFace):
    def onStart(self): self.update(0)


class Effect_14_WipeFaceY(HelperEffect_WipeFace):
    def onStart(self): self.update(1)


class Effect_15_WipeFaceZ(HelperEffect_WipeFace):
    def onStart(self): self.update(2)


class Effect_16_WipeFaceXYZ(HelperEffect_WipeFace):
    def onStart(self):
        self.progress_percent = 0
        self.pos = 0
        self.update(self.pos)

    def onAnimate(self, dt):
        self.progress_percent += dt / self.ca.period
        if self.progress_percent >= 1:
            self.pos = (self.pos + 1) % 3
            self.update(self.pos)
            self.progress_percent = 0


class Effect_17_WipeFaceVertical(Effect):
    def onStart(self):
        for xyz in itertools.product(range(4), repeat=3):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/2)
            self.ca[xyz].set_phase_percent(1-sum(xyz)/20)


class Effect_18_WipeInOut(Effect):
    def onStart(self):
        def o(xyz, phase):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/2)
            self.ca[xyz].set_phase_percent(phase/10 + 1/2)
        helper_inout(o)


class Effect_19_WipeOutIn(Effect):
    def onStart(self):
        def o(xyz, phase):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/2)
            self.ca[xyz].set_phase_percent(phase/10 + 1/2)
        helper_outin(o)


class Effect_20_WipeEdges(Effect):
    def onStart(self):
        def o(xyz, phase):
            self.ca[xyz].set_colors()
            self.ca[xyz].set_duty_cycle(1/2)
            self.ca[xyz].set_phase_percent(phase/20)
        for i in range(64):
            self.ca[i].set_colors(2, 2)
        helper_edges(o)


class Effect_21_BlinkHalf(Effect):
    def onStart(self):
        for i in range(64):
            self.ca[i].set_colors()
            self.ca[i].set_duty_cycle(1/2)
            self.ca[i].set_phase_percent(0)
