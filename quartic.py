from polynomial import Poly
from cplxnums import cplx, powFrac
from math import sqrt
from quadratics import Quadratic
from cubics import Cubic

class Quartic(Poly):
    significant_figures = 4

    def __new__(cls, coeffs):
        if len(coeffs) - 1 != 4:
            return "Not quartic"
        else:
            if len(coeffs) - 1 == 4 and coeffs[4] == 0:
                return "Not quartic"
            return super().__new__(cls, coeffs)
    
    def __init__(self, coeffs):
        super().__init__(coeffs)

    def toDepressed(self):
        e = self.coeff(0)
        d = self.coeff(1)
        c = self.coeff(2)
        b = self.coeff(3)
        a = self.coeff(4)

        alpha = -3*(b**2)/(8*(a**2)) + c/a 
        beta = (b**3)/(8*(a**3)) - (b*c)/(2*(a**2)) + d/a 
        gamma = (-3*(b**4))/(256*(a**4)) + (c*(b**2))/(16*(a**3)) - (b*d)/(4*(a**2)) + e/a 

        return Quartic([gamma, beta, alpha, 0, 1])

    def zeroesBiQuad(self):
        if self.coeff(1) == 0 and self.coeff(3) == 0:
            qrt_zros = []

            c = self.coeff(0)
            b = self.coeff(2)
            a = self.coeff(4)
            
            quadratic = Quadratic([c, b, a]) 
            qd_zros = quadratic.zeroes()

            if all(isinstance(zro, (int, float)) for zro in qd_zros):
                for zro in qd_zros:
                    qrt_zros += [abs(sqrt(zro))] + [-abs(sqrt(zro))]

                return qrt_zros

            if all(isinstance(zro, cplx) for zro in qd_zros):
                for zro in qd_zros:
                    zro_sqrt = powFrac(zro, 1/2)
                    qrt_zros += [zro_sqrt] + [cplx([-1, 0])*zro_sqrt]

                return qrt_zros
        return

    def zeroes(self):

        depressed = self.toDepressed()
        if round(depressed.coeff(1), Quartic.significant_figures) == 0:
            return self.zeroesBiQuad()

        depr_coeffs = depressed.coeffs 
        c = depr_coeffs[0]
        b = depr_coeffs[1]
        a = depr_coeffs[2]

        intermediate_cubic = Cubic([a*c - (1/4)*(b**2), -2*c, -a, 2])
        cubic_zro = intermediate_cubic.zeroes()[0]

        in_radical = cplx([2, 0]) * cubic_zro - cplx([a, 0])
        in_radical_2 = cplx([-2, 0]) * cubic_zro - cplx([a, 0])
        radical_1 = powFrac(in_radical, 1/2)
        radical_2 = powFrac(in_radical_2 + cplx([2*b, 0])/powFrac(in_radical, 1/2), 1/2)
        radical_3 = powFrac(in_radical_2 - cplx([2*b, 0])/powFrac(in_radical, 1/2), 1/2)
        
        soln_1 = cplx([-1/2, 0]) * radical_1 + cplx([1/2, 0]) * radical_2
        soln_2 = cplx([-1/2, 0]) * radical_1 + cplx([-1/2, 0]) * radical_2
        soln_3 = cplx([1/2, 0]) * radical_1 + cplx([1/2, 0]) * radical_3
        soln_4 = cplx([1/2, 0]) * radical_1 + cplx([-1/2, 0]) * radical_3

        translate_by = self.coeff(3)/(4*self.coeff(4))
        translate_by = cplx([translate_by, 0])

        return (soln_1 - translate_by, soln_2 - translate_by, soln_3 - translate_by, soln_4 - translate_by)
