# Introduction

Univariate functions are functions in one variable. This document concerns univariate polynomials and rational functions. Work on the multivariate case is forthcoming.

A rational function is a quotient of one polynomial by another. It is not necessarily polynomial itself. E.g., the function $x\mapsto 1/x$ is rational but not polynomial. The constant function $x \mapsto 1$ is polynomial however. Consequently, since any polynomial $x\mapsto f(x)$ can be written 

```{math}

x\mapsto \frac{f(x)}{1(x)} = \frac{f(x)}{1}

```

i.e., as a quotient of polynomials, any polynomial is rational.

## Outline

The GitHub repository `KshkB/Univariates` contains files generating this Jupyter book and the modules implementing univariate polynomials and rational functions as Python class types. The purpose of this documentation is describe and demonstrate these classes and their methods.

Below is a brief outline of what is contained in this documentation. 

### Polynomials

Polynomials of any degree are instances of the class `Poly`. This class is coded in the module `polynomial.py`. Currently available methods are:

- evaluation on both real and complex numbers;
- addition, multiplication and division;
- differentiation to any order;
- integration to any order;
- area under the curve;
- composition;
- the Sylvester matrix;
- resultants and the discriminant;
- Euclid's algorithm for finding the greatest common divisor for polynomials.

### Rational function methods

The class `Rational` in `rational.py` codes for rational functions. That is, instances of `Rational` are rational functions. Methods available on this class are:

- evaluation;
- addition, multiplication, polynomial long division;
- differentiation to any order;
- composition;
- simplification. 

### Complex numbers

The fundamental theorem of algebra necessitates the use of complex numbers. As a class, complex numbers are coded as `cplx` in the module `cplxnums.py`. Methods available on `cplx` are:

- arithmetic (addition, subtraction, multiplication, division);
- representation on $2\times2$ real matrices;
- polar transformation;
- the roots of unity;
- fractional powers.

### Low degree polynomials 

By low degree, it is meant in degrees $d = 2, 3, 4$. These degrees are special since it is only here where general algebraic formulae exist for the zeroes (or, roots).


```{note}

Linear polynomials are not studied separately.

```

The module `quadratics.py` encodes quadratic (degree two) polynomials as `Quadratic`. 

The module `cubics.py` encodes the cubic polynomials (degree three) as `Cubic`.

The module `quartics.py` encodes quartic polynomials (degree four) as `Quartic`.


Each of these polynomials of specified degree are, of course, polynomials. The classes `Quadratic`, `Cubic` and `Quartic` are accordingly coded as subclasses of `Poly`. A common method among each of these classes is `zeroes()`. Calling this on any instance returns a list of all zeroes of the instance. 

```{note}

While `Quadratic`, `Cubic` and `Quartic` are subclasses of `Poly`, the method `zeroes()` is not callable on instances `Poly`.  

```