# Univariates

The `main` branch of this repository contains modules for studying polynomials and rational functions in one variable. These are coded as Python class types. Included are modules for studying:

- polynomials;
- rational functions;
- complex numbers;
- quadratics;
- cubics;
- quartics.

The `gh-pages` branch contains files generating the Jupyter book. This book describes and demonstrates the univariate functions in `main`.

See [here](https://kshkb.github.io/Univariates/intro.html) for the online Jupyter book.

## Module imports

The module `cplxnums.py` requires the `numpy` library in forming and returning matrix representations of complex numbers.

The module `polynomial.py` imports the `numpy` library and `cplxnums.py` for implementing polynomial long division and for evaluation over complex numbers.

The module `rational.py` imports `polynomial.py` in forming the numerator and denominator as polynomials.

The modules `quadratics.py`, `cubics.py` and `quartics.py` import `polynomial.py`, `cplxnums.py` and draw on the `math` library for representing and studying zeroes.
