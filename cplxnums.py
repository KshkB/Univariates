import numpy as np
from math import sqrt, acos, inf, cos, sin, pi

class cplx:

    significant_figures = 4
    cplx_unit = [0, 1]

    def __new__(cls, coeffs):
        if isinstance(coeffs, (list, tuple)):
            if len(coeffs) > 2 or len(coeffs) < 2:
                return "Invalid input"
            elif len(coeffs) == 2:
                return super().__new__(cls)
        else:
            return "Invalid input"

    def __init__(self, coeffs):
        
        self.coeffs = coeffs
        self.re = coeffs[0]
        self.im = coeffs[-1]
        self.normsq = self.re**2 + self.im**2

    def mtrx(self):
        mtrx = np.matrix([[self.re, -self.im], [self.im, self.re]])
        return mtrx

    def __repr__(self):
        return f"{self.__class__.__name__}({self.coeffs})"

    def __str__(self):
        self.re = round(self.re, cplx.significant_figures)
        self.im = round(self.im, cplx.significant_figures)
        if self.im >= 0:
            return f"{self.re} + {self.im}i"
        if self.im < 0:
            string_image = str(self.im)
            string_image = string_image[1:]
            return f"{self.re} - {float(string_image)}i"

    def __add__(self, other):
        added_real = self.re + other.re
        added_im = self.im + other.im
        return cplx([added_real, added_im])

    def __mul__(self, other):
        self_mrtx = np.matrix([[self.re, -self.im], [self.im, self.re]])
        other_mrtx = np.matrix([[other.re, -other.im], [other.im, other.re]])
        

        prod = np.matmul(self_mrtx, other_mrtx)
        cplx_unit_neg = np.matrix([[cplx.cplx_unit[0], cplx.cplx_unit[-1]], [-cplx.cplx_unit[-1], cplx.cplx_unit[0]]])
        prod_re = (1/2) * np.trace(prod)
        prod_im = (1/2) * np.trace(np.matmul(cplx_unit_neg, prod))
        
        return cplx([prod_re, prod_im])

    def __sub__(self, other):
        other = cplx([-1, 0]) * other 
        return self + other

    def __pow__(self, n):
        if n == 0:
            return cplx([1, 0])

        if n == 1:
            return self 
        factor = self
        while (n > 1):
            self *= factor 
            n += -1
        
        return self

    def __truediv__(self, other):
        self_mrtx = self.mtrx()
        other_mtrx = other.mtrx()
        other_mtrx_inv = np.linalg.inv(other_mtrx)

        prod = np.matmul(self_mrtx, other_mtrx_inv)
        cplx_unit_neg = np.matrix([[cplx.cplx_unit[0], cplx.cplx_unit[-1]], [-cplx.cplx_unit[-1], cplx.cplx_unit[0]]])

        prod_re = (1/2) * np.trace(prod)
        prod_im = (1/2) * np.trace(np.matmul(cplx_unit_neg, prod))

        return cplx([prod_re, prod_im])

    def __eq__(self, other):
        if round(self.re, cplx.significant_figures) == round(other.re, cplx.significant_figures) and round(self.im, cplx.significant_figures) == round(other.im, cplx.significant_figures):
            return True
        return False

    def conjugate(self):
        re = self.re 
        im = -self.im
        return cplx([re, im])

    def toPolar(self):
        rad = abs(sqrt(self.normsq))
        azimuth = inf
        if rad != 0:
            if self.im >= 0:
                azimuth = acos(self.re/rad)
                return rad, azimuth
            if self.im < 0:
                azimuth = -acos(self.re/rad)
                return rad, azimuth
        return rad, azimuth

def cis(radius, angle):
    return cplx([radius, 0]) * cplx([cos(angle), sin(angle)])

def rootsUnity(n):
    if n == 0:
        return None 
    if n > 0:
        roots = []
        const = 2 * pi / n
        for k in range(n):
            arg_1 = cos(const * k)
            arg_2 = sin(const * k)
            roots += [cplx([arg_1, arg_2])]

        return roots
    if n < 0:
        n = -n
        return rootsUnity(n)

def powFrac(cx, q):
    if isinstance(cx, cplx):
        cx = cx.toPolar()
        rad = cx[0]
        rad = rad**q

        angle = cx[-1]
        angle = angle*q 

        return cis(rad, angle)
