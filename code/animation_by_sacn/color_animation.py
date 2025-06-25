#!/usr/bin/env python3

from cube_sacn_abtraction import coord_3d_to_linear
from effects import all_effects


def period_decode(v: int) -> float:
    return 1 if v == 0 else 0.5 + (9.5) * v/255


class ColorAnimation:
    def __init__(self, cube_animator):
        self.cube = cube_animator
        self.color1 = 0
        self.color2 = 0
        self.duty_cycle = 1
        self.progress_percent = 0

    def _color(self, c, d):
        if c is None:
            c = d
        if c == 0:
            c = (0, 0, 0)
        elif c == 1:
            c = self.cube.color1
        elif c == 2:
            c = self.cube.color2
        return c

    def set_colors(self, c1=None, c2=None):
        self.color1 = c1
        self.color2 = c2

    def set_duty_cycle(self, p):
        self.duty_cycle = min(max(0, p), 1)

    def set_phase_percent(self, p):
        self.progress_percent = min(max(0, p), 1)

    def animate(self, dt):
        self.progress_percent += dt / self.cube.period
        if self.progress_percent > 1:
            self.progress_percent %= 1
        if self.progress_percent > self.duty_cycle:
            c = self._color(self.color2, 2)
        else:
            c = self._color(self.color1, 1)
        return c


class CubeAnimator:
    def __init__(self, cubectrl):
        self.cubectrl = cubectrl

        self.color1 = (0, 0, 0)
        self.color2 = (0, 0, 0)
        self.period = 2

        self.anims = [ColorAnimation(self) for _ in range(64)]

        self.effects = all_effects(self)
        self.fxnb = 0
        self.fx = None

    def setColors(self, c1=None, c2=None):
        changed = False
        if c1 is None:
            c1 = (0, 0, 0)
        if c1 != self.color1:
            self.color1 = c1
            changed = True
            if self.fx:
                self.fx.onColor1Changed()
        if c2 is None:
            c2 = (0, 0, 0)
        if c2 != self.color2:
            self.color2 = c2
            changed = True
            if self.fx:
                self.fx.onColor2Changed()
        if changed:
            if self.fx:
                self.fx.onColorsChanged()

    def setFx(self, n):
        if n == self.fxnb:
            return
        if self.fx:
            self.fx.onStop()
        if n > 0 and n <= len(self.effects):
            self.fxnb = n
            self.fx = self.effects[n-1]
            self.fx.onStart()
        else:
            self.fxnb = 0
            self.fx = None
            for a in self.anims:
                a.set_colors(0, 0)

    def setPeriod(self, p):
        p = period_decode(p)
        if self.period != p:
            self.period = p
            if self.fx:
                self.fx.onPeriodChanged()

    def animate(self, dt):
        if self.fx:
            self.fx.onAnimate(dt)
        for i, a in enumerate(self.anims):
            self.cubectrl.tals[i] = a.animate(dt)
        self.cubectrl.blit()

    def __getitem__(self, k):
        if isinstance(k, int):
            return self.anims[k]
        else:
            return self.anims[coord_3d_to_linear(*k)]
