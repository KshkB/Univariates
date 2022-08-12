from polynomial import Poly
from cplxnums import cplx
from math import sqrt


class Quadratic(Poly):
    
    def __new__(cls, coeffs):
        if len(coeffs) - 1 != 2:
            return "Not quadratic"
        else:
            if len(coeffs) - 1 == 2 and coeffs[2] == 0:
                return "Not quadratic"
            return super().__new__(cls, coeffs)
    
    def __init__(self, coeffs):
        super().__init__(coeffs)
        c = coeffs[2]
        b = coeffs[1]
        a = coeffs[0]

        self.disc = b**2 - 4 * a * c
         
    def zeroes(self):
        a = self.coeff(self.degree)
        b = self.coeff(self.degree - 1)

        if self.disc >= 0:
        
            soln_1 = (1/(2*a)) * (- b + sqrt(self.disc))
            soln_2 = (1/(2*a)) * (-b - sqrt(self.disc))

            return soln_1, soln_2

        if self.disc < 0:

            half_b = cplx([(1/(2*a)) * b, 0])
            sqrt_disc = cplx(cplx.cplx_unit) * cplx([(1/(2*a)) * sqrt(-self.disc), 0])
            
            soln_1 = cplx([0, 0])- half_b + sqrt_disc
            soln_2 = cplx([0, 0]) - half_b - sqrt_disc

            return soln_1, soln_2
            