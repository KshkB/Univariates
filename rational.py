from polynomial import Poly

class Rational:
    
    def __new__(cls, numerator, denominator):
        
        if isinstance(numerator, (tuple, list)) and isinstance(denominator, (tuple, list)):
            if all(isinstance(x, (int, float)) for x in numerator) and all(isinstance(x, (int, float)) for x in denominator):
                #if all(x == 0 for x in denominator):
                #    print("WARNING: Undefined")
                return super().__new__(cls)
            else:
                return "One or more of the coefficients is neither an integer or float"
        else:
            return "Invalid data type. Input tuples or lists"

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        self.numdeg = len(numerator)-1
        self.denomdeg = len(denominator) - 1

    def eval(self, num):
        numerator_eval = Poly(self.numerator).eval(num)
        denominator_eval = Poly(self.denominator).eval(num)
        if denominator_eval != 0:
            return numerator_eval/denominator_eval
        else:
            return "Undefined"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        numerator = self.numerator
        denominator = self.denominator
        return f"numerator: {Poly(numerator)}\ndenominator: {Poly(denominator)}"

    def __add__(self, other):

        self_numer_poly = Poly(self.numerator)
        self_denom_poly = Poly(self.denominator)

        other_numer_poly = Poly(other.numerator)
        other_denom_poly = Poly(other.denominator)

        sum_numer = self_numer_poly * other_denom_poly + other_numer_poly * self_denom_poly
        sum_denom = self_denom_poly * other_denom_poly

        return Rational(sum_numer.coeffs, sum_denom.coeffs)

    def __mul__(self, other):

        self_numer_poly = Poly(self.numerator)
        self_denom_poly = Poly(self.denominator)

        other_numer_poly = Poly(other.numerator)
        other_denom_poly = Poly(other.denominator)

        mul_numer = self_numer_poly * other_numer_poly
        mul_denom = self_denom_poly * other_denom_poly

        return Rational(mul_numer.coeffs, mul_denom.coeffs)

    def __sub__(self, other):
        other = Rational([-1], [1]) * other
        return self + other

    def __pow__(self, n):
        if n == 0:
            return Rational([1], [1])

        if n == 1:
            return self 

        factor = self
        while (n > 1):
            self *= factor 
            n += -1
        
        return self

    def __truediv__(self, other):
        
        other_numinv = other.denominator
        other_denominv = other.numerator

        return self * Rational(other_numinv, other_denominv) 

    def diff(self):
        
        numerator = self.numerator
        denominator = self.denominator

        der_numer = Poly(numerator).diff() * Poly(denominator) - Poly(numerator) * Poly(denominator).diff()
        der_denom = Poly(denominator)**2

        #return repr(Poly(numerator).diff()), repr(Poly(numerator) * Poly(denominator).diff())
        return Rational(der_numer.coeffs, der_denom.coeffs)

    def Hdiff(self, n):
        if n == 0:
            return self
        
        if n == 1:
            return self.diff()

        while (n>1):
            n += -1
            self = self.diff()
            return self.Hdiff(n)

    def composeWith(self, other):
        self_numerator = Poly(self.numerator)
        self_denominator = Poly(self.denominator)

        composite_numer = Rational([0], [1])
        for i in range(self.numdeg + 1):
            composite_numer += Rational([self_numerator.coeff(i)], [1]) * (other**i)

        composite_denom = Rational([0], [1])
        for i in range(self.denomdeg + 1):
            composite_denom += Rational([self_denominator.coeff(i)], [1]) * (other**i)

        return composite_numer/composite_denom

    def simplify(self):
        poly_num = Poly(list(self.numerator))
        poly_denom = Poly(list(self.denominator))

        gcd = Poly.gcd(poly_num, poly_denom)
        
        num_div = poly_num / gcd 
        new_numerator = num_div[0]
        
        denom_div = poly_denom / gcd 
        new_denom = denom_div[0]

        return Rational(new_numerator.coeffs, new_denom.coeffs)
