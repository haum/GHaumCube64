#!/usr/bin/env python3

import time
import sacn
from timeit import default_timer as timer
from cube_sacn_abtraction import CubeSacnController
from color_animation import CubeAnimator
from console import Console


def main():
    try:
        receiver = sacn.sACNreceiver()
        receiver.start()
        receiver.join_multicast(3)

        t_step = 1/30
        cubectrl = CubeSacnController('SacnAnim', bind_port=5569)
        ca = CubeAnimator(cubectrl)

        data = [[0, 0, 0, 0, 0, 0, 0, 0]]
        console = Console(data)

        @receiver.listen_on('universe', universe=3)
        def callback(packet):
            if packet.dmxStartCode == 0x00:  # ignore non-DMX-data packets
                data[0] = list(packet.dmxData[:8])

        t_now = t_target = timer()
        while True:
            t_last, t_now = t_now, timer()
            dt = t_now - t_last

            ca.setColors(data[0][0:3], data[0][3:6])
            ca.setFx(data[0][6])
            ca.setPeriod(data[0][7])

            console.process()
            ca.animate(dt)

            t_target += t_step
            t_sleep = t_target - timer()
            if t_sleep > 0:
                time.sleep(t_sleep)

    except KeyboardInterrupt:
        cubectrl.stop()
        receiver.leave_multicast(3)
        receiver.stop()


if __name__ == '__main__':
    main()
