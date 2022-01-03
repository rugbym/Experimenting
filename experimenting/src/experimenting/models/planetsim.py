import numpy as np
import matplotlib.pyplot as plt
from time import time
from statistics import mean, stdev
import math
from scipy import constants


class orbit:
    def __init__(self):
        self.distance_start = 10
        self.distance = self.distance_start
        self.m1 = 10 ** 10
        self.m2 = 10 ** 50
        self.rlargestart = 0
        self.rsmallstart = self.rlargestart + self.distance_start

        self.v_start = 0
        self.v_1_old = 0
        self.v_2_old = 0
        self.dt = 0.1
        self.t = 0

    def force(self):
        F = constants.G * self.m1 * self.m2 / (self.r ** 2)

    def motion(self, othermass, distance, r_old, v_old):

        a = constants.G * othermass / (distance) ** 2
        v_new = v_old + a * self.dt
        r_new = r_old + v_new * self.dt
        return r_new, v_new

    def sim(self):
        self.t_list, self.rsmall_list, self.rlarge_list = [], [], []

        for t in np.arange(0, 100, self.dt):
            self.t = t
            self.rsmall, self.v_1_old = self.motion(
                -self.m1, self.distance, self.rsmallstart, self.v_1_old
            )
            self.rlarge, self.v_2_old = self.motion(
                self.m2, self.distance, self.rlargestart, self.v_2_old
            )
            self.t_list.append(t), self.rsmall_list.append(
                self.rsmall
            ), self.rlarge_list.append(self.rlarge)
            self.distance = self.rsmall - self.rlarge

            # print(f"time {t=}, distance {self.distance}")
            self.plot()
        plt.show()

    def plot(self, realtime=False):

        if realtime:
            plt.plot(self.t, self.rsmall, "o")
            plt.plot(self.t, self.rlarge, "o")
            plt.ylim(0, 10)
            plt.draw()
            plt.pause(0.001)
            plt.clf()
        else:
            plt.plot(self.t_list, self.rsmall_list, "o")
            plt.plot(self.t_list, self.rlarge_list, "o")


if __name__ == "__main__":
    sim = orbit()
    sim.sim()
