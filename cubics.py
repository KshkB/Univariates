from polynomial import Poly
from cplxnums import cplx, powFrac, rootsUnity
from math import sqrt

class Cubic(Poly):
    cube_roots = rootsUnity(3)

    def __new__(cls, coeffs):
        if len(coeffs) - 1 != 3:
            return "Not a cubic"
        else:
            if len(coeffs) - 1 == 3 and coeffs[3] == 0:
                return "Not a cubic"
            return super().__new__(cls, coeffs)

    def __init__(self, coeffs):
        super().__init__(coeffs)
        self.coeffs = coeffs

        d = coeffs[0]
        c = coeffs[1]
        b = coeffs[2]
        a = coeffs[3]

        self.disc = (b**2)*(c**2) - 4*a*(c**3) - 4*(b**3)*d - 27*(a**2)*(d**2) + 18*a*b*c*d
        
    def toDepressed(self):

        d = self.coeff(0)
        c = self.coeff(1)
        b = self.coeff(2)
        a = self.coeff(3)
        
        p = (3*a*c - b**2)/(3*(a**2))
        q = (2*(b**3) - 9*a*b*c + 27*(a**2)*d)/(27*(a**3))
        return Cubic([q, p, 0, 1])

    def zeroes(self):
        zros = []
        d = self.coeff(0)
        c = self.coeff(1)
        b = self.coeff(2)
        a = self.coeff(3)
        
        if self.disc == 0:
            if b**2 == 3 * a * c:
                zro = cplx([-b/(3*a), 0])
                zros += [zro]*3
                return zros
            else:
                double_root = (9 * a * d - b * c)/(2*(b**2 - 3 * a * c))
                double_root = cplx([double_root, 0])

                simple = (4*a*b*c - 9*(a**2)*d - b**3)/(a*(b**2 - 3*a*c))
                simple = cplx([simple, 0])

                zros += [double_root]*2 + [simple]
                return zros
        else:
            prime_cube_root = Cubic.cube_roots[-1]

            del_0 = b**2 - 3*a*c 
            del_1 = 2*(b**3) - 9*a*b*c + 27*(a**2)*d 

            if del_1**2 - 4*(del_0**3) < 0:
                const_cubed = cplx([del_1/2, 0]) + cplx([0, (1/2)*sqrt(-del_1**2 + 4*(del_0**3))])

            if del_1**2 - 4*(del_0**3) > 0:
                const_cubed = cplx([del_1/2, 0]) + cplx([(1/2)*sqrt(del_1**2 - 4*(del_0**3)), 0])

            const = powFrac(const_cubed, 1/3)
            a = cplx([a, 0])
            b = cplx([b, 0])
            del_0 = cplx([del_0, 0])

            for k in range(3):
                prime_multiple = prime_cube_root**k
                rt = cplx([-1, 0])/(cplx([3, 0])*a) * (b + const*prime_multiple + del_0/(const*prime_multiple))
                zros += [rt]
                
            return zros
