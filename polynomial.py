from collections import defaultdict
import numpy as np
import cplxnums as cplx

class Poly:

    significant_figures = 4

    def __new__(cls, coeffs):
        if isinstance(coeffs, (list, tuple)):
            if all(isinstance(x, (int, float)) for x in coeffs):
                l = len(coeffs)
                if l > 1:
                    for i in reversed(coeffs[1:]):
                        if not i:
                            del coeffs[-1]
                        else:
                            break
                    return super().__new__(cls)
                if l == 1:
                    return super().__new__(cls)
            else:
                return "One or more of the coefficients is neither an integer or float. Try again."
        if isinstance(coeffs, (int, float)):
            coeffs = [coeffs]
            return super().__new__(cls)
        else:
            return "The coefficients form neither a list or set tuple. Try again."

    def __init__(self, coeffs):
        self.coeffs = coeffs
        if all((x==0) for x in self.coeffs):
            self.degree = 0
        else:      
            self.degree = len(coeffs) - 1

    def coeff(self, i):
        try:
            return self.coeffs[i]
        except IndexError:
            return

    def __repr__(self):
        return f"{self.__class__.__name__}({self.coeffs})"

    def __str__(self):

        if all((x == 0) for x in self.coeffs):
            return "The zero polynomial."

        first_nonzero = next((i for i, x in enumerate(self.coeffs) if x), None)

        first = self.coeff(first_nonzero)
        first = round(first, Poly.significant_figures)
        if first > 0:
            string = f"{first}x^{first_nonzero} "
        if first < 0:
            first_str = str(first)
            string = f"{first_str[0]}{first_str[1:]}x^{first_nonzero} "

        for i, c in enumerate(self.coeffs):
            c = round(c, Poly.significant_figures)
            if i > first_nonzero:
                if c == 0:
                    pass
                if c > 0:
                    string += f"+ {c}x^{i} "
                if c < 0:
                    c = str(c)
                    string += f"{c[0]} {c[1:]}x^{i} "
        
        return string

    def eval(self, num):
        val = 0
        for i in range(self.degree + 1):
            val += self.coeff(i) * num**i
    
        return val

    def __add__(self, other):
        if isinstance(other.coeffs, (list, tuple)):
            if all(isinstance(x, (int, float)) for x in other.coeffs):
                deg_self = self.degree
                deg_other = other.degree
                added_dict = {}

                if deg_self < deg_other:
                    min_deg = deg_self
                    for i in range(min_deg + 1):
                        added_dict[i] = self.coeff(i) + other.coeff(i)
                    for j in range(min_deg+1, deg_other + 1):
                        added_dict[j] = other.coeff(j)

                if deg_other < deg_self:
                    min_deg = deg_other
                    for i in range(min_deg + 1):
                        added_dict[i] = self.coeff(i) + other.coeff(i)
                    for j in range(min_deg+1, deg_self + 1):
                        added_dict[j] = self.coeff(j)
                
                if deg_self == deg_other:
                    min_deg = deg_self
                    for i in range(min_deg + 1):
                        added_dict[i] = self.coeff(i) + other.coeff(i)

                return Poly([added_dict[coeff_key] for coeff_key in added_dict])    
            else:
                return "At least one of the coefficients is neither an integer or float type."               
        else:
            return "One of the arguments is neither a list or tuple."
             
    def __mul__(self, other):
         if isinstance(other.coeffs, (list, tuple)):
            if all(isinstance(x, (int, float)) for x in other.coeffs):
                coeff_mat = []
                for coeff in self.coeffs:
                    row = [coeff * coeff_other for coeff_other in other.coeffs]
                    coeff_mat.append(row)

                new_coeffs = defaultdict(float)
                l = len(coeff_mat)
                for i in range(l):
                    row = coeff_mat[i]
                    for j in range(len(row)):
                        new_coeffs[i+j] += coeff_mat[i][j]

                new_coeffs_arr = [new_coeffs[new_coeff] for new_coeff in new_coeffs]
                return Poly(new_coeffs_arr)

    def __sub__(self, other):
        negative = [(-1)* coeff for coeff in other.coeffs]
        return self + Poly(negative)

    def __pow__(self, n):
        if n == 0:
            return Poly([1])

        if n == 1:
            return self 
        factor = self
        while (n > 1):
            self *= factor 
            n += -1
        
        return self

    def __eq__(self, other):
        if self.degree == other.degree:
            if all(round(self.coeff(i), Poly.significant_figures) == round(other.coeff(i), Poly.significant_figures) for i in range(self.degree+1)):
                return True
            else:
                return False
        else:
            return False

    def __truediv__(self, other):
        self_reverse = list(reversed(self.coeffs))
        other_reverse = list(reversed(other.coeffs))

        np_poly_numerator = np.array(self_reverse)
        np_poly_denominator = np.array(other_reverse)

        np_div = np.polydiv(np_poly_numerator, np_poly_denominator)
        
        poly_divisor = reversed(np_div[0].tolist())
        poly_remainder = reversed(np_div[-1].tolist())

        results = [Poly(list(poly_divisor)), Poly(list(poly_remainder))]

        return results

    def diff(self):
        diff_poly = {}
        for i in range(self.degree + 1):
            diff_poly[i] = i*self.coeff(i)
        
        diff_poly_arr = [diff_poly[i] for i in diff_poly]
        if len(diff_poly_arr) > 0:
            diff_poly_arr = diff_poly_arr[1:]
        if len(diff_poly_arr) == 0:
            diff_poly_arr = [0]

        return Poly(diff_poly_arr)

    def Hdiff(self, n):
        try:
            if n == 0:
                return self
        
            if n == 1:
                return self.diff()

            while (n>1):
                n += -1
                self = self.diff()
                return self.Hdiff(n)
        except TypeError:
            return "The zero polynomial"

    def intgr(self):
        integrated = {0:0}
        for i in range(self.degree+1):
            integrated[i+1] = self.coeff(i)/(i+1)

        return Poly([integrated[new_coeff] for new_coeff in integrated])

    def Hintgr(self, n):
        if n == 0:
            return self
        if n == 1:
            return self.intgr()

        while (n > 1):
            n += -1
            self = self.intgr()
            return self.Hintgr(n)

    def AreaUnder(self, rng):
        if isinstance(rng, (list, tuple)):
            if all(isinstance(x, (int, float)) for x in rng):
                if len(rng) == 2:
                    first = rng[0]
                    last = rng[-1]
                    intgrl = self.intgr()
                    if first == last:
                        return 0
                    else:
                        return intgrl.eval(last) - intgrl.eval(first)
                else:
                    return "Invalid range"
            else:
                return "Invalid range"
        else:
            return "Invalid range"
    
    def composeWith(self, other):
        curr_pol = Poly([0])
        for i in range(self.degree + 1):
            curr_pol += Poly([self.coeff(i)]) * (other**i)
        return curr_pol

    def SylvesterMatrix(self, other):
        mtrx_rows_1 = {}
        for i in range(other.degree):
            mtrx_rows_1[i] = [0]*i + self.coeffs + [0]*(other.degree -1 - i)

        mtrx_rows_2 ={}
        for i in range(self.degree):
            mtrx_rows_2[i] = [0]*i + other.coeffs + [0]*(self.degree -1 - i)
        
        mtrx = [
            mtrx_rows_1[row] for row in mtrx_rows_1
        ]

        mtrx += [
            mtrx_rows_2[row] for row in mtrx_rows_2
        ]
    
        return mtrx

    def resultant(self, other):
        #significant_figures = 4
        mtrx = Poly.SylvesterMatrix(self, other)
        mtrx = np.array([mtrx])
        return np.linalg.det(mtrx)[0]

    def discriminant(self):
        der = self.diff()
        resultant = Poly.resultant(self, der)
        mult_factor_sign = (-1)**(self.degree * (self.degree - 1)/2)
        mult_factor_coeff = 1/self.coeff(self.degree)

        return round(mult_factor_sign * mult_factor_coeff * resultant, Poly.significant_figures)

    def cplxEval(self, arg):
        if isinstance(arg, cplx):
            val = cplx([0, 0])
            for i in range(self.degree + 1):
                coeff = self.coeff(i)
                coeff = cplx([coeff, 0])
                val += coeff*(arg**i)
            return val
        else:
            return self.eval(arg)

    def gcd(self, other):
        gcd = Poly([1])
        
        if self.degree >= other.degree:
            
            if other.degree == 0:
                gcd = Poly([other.coeff(0)])
                return gcd

            if other.degree == 1:
                division = self/other
                remainder = division[-1]
                if remainder == Poly([0]):
                    gcd = other
                    return gcd
                return gcd   
            
            self_divided = self / other
            remainder = self_divided[-1]

            if remainder == Poly([0]*(remainder.degree + 1)):
                gcd = other
                return gcd

            else:
                other_divided = other / remainder 
                other_remainder = other_divided[-1]
                if other_remainder == Poly([0]*(other_remainder.degree + 1)):
                    gcd = remainder 
                    return gcd 
                else:
                    new_self = remainder 
                    new_other = other_remainder
                    return new_self.gcd(new_other)
        
        else:
            return other.gcd(self)
                

