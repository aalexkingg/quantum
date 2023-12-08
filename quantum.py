import scipy as sci
import numpy as np

h = sci.constants.h
h_bar = sci.constants.hbar


class Particle:
    def __init__(self, m, E, a):
        self.m = m
        self.a = a
        self.E = E
        self.r_hat = 1
        self.p = h_bar * self.k * self.r_hat
        self._V = 0
        self._k = 0

    @property
    def k(self):
        if self._V > 0:
            # Region of non-zero potential
            self._k = np.sqrt(2 * self.m * (self.V - self.E)) / h_bar
        else:
            # Region of zero potential
            self._k = np.sqrt(2 * self.m * self.E) / h_bar

        return self._k

    @property
    def V(self): return self._V
    @V.setter
    def V(self, V): self._V = V



    def E_n(self, n):
        return (h_bar**2 * np.pi**2) / (8 * self.m * self.a**2) * n**2

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


class WaveFunction:
    def __init__(self, x):
        self.x = x

    def conjugate(self):
        pass

    def differential(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass