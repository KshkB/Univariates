#!/usr/bin/env python
# coding: utf-8

# # Polynomials (basics)
# 
# In one variable $x$, a polynomial $x \stackrel{f}{\mapsto} y$ is given by a finite sum,
# 
# ```{math}
# 
# y = f(x) = \sum_{i = 0}^n a_ix^i.
# 
# ```
# 
# Any polynomial $f$ is specified by a finite string of parameters $(a_0, a_1, \ldots, a_n)$ called its *coefficients*. If the coefficients are real numbers, $f$ is a *real* polynomial; if they are complex, $f$ is a *complex* polynomial; if they are integers, $f$ is an *integral* polynomial and if they are rational numbers, $f$ is a *rational* polynomial.
# 
# ```{warning}
# 
# Rational polynomials are not to be confused with rational *functions*.
# 
# ```
# 

# ## Mathematical background
# 
# These prefixes for $f$ (real, complex, integral, rational) are properties of its coefficients. They do not imply anything about the intermediate $x$. Here $x$ is a coordinate and could be valued in any algebraic structure $R$ where the *scalars* in $R$ are one of these prefixes. That is, it must make sense to form $ax$ and $ax + bx$ for scalars $a, b$, which may be real, complex, integral, rational, etc.
# 
# Let $\mathbb K$ be the ring (usually, field) of scalars. So $\mathbb K$ could be $\mathbb R, \mathbb C, \mathbb Z, \mathbb Q$. Formally, the intermediate $x$ is a coordinate on *affine space over $\mathbb K$*, denoted $\mathbb A_{\mathbb K}$. That is, it is a function on $\mathbb A_{\mathbb K}$. 
# 
# ```{note}
# 
# We distinguish here between spaces and functions on spaces. So here, $\mathbb A_{\mathbb K}$ is a space in the topological sense while $x$ is a function on $\mathbb A_{\mathbb K}$.
# 
# ```
# 
# Unlike for spaces, the set of functions on a space forms a nice algebraic structure - a *ring*. It makes sense to add and multiply functions; it does not necessarily make sense to add and multiply points in a space. The set of (suitably global) functions on $\mathbb A_{\mathbb K}$ is denoted $\mathbb K[x]$. It is precisely the ring of *all polynomials in one variable $x$ with coefficients in $\mathbb K$*.
# 
# There is a formal, duality relation between the affine space $\mathbb A_{\mathbb K}$ and the ring of polynomials $\mathbb K[x]$. The space $\mathbb A_{\mathbb K}$ is the *spectrum* of $\mathbb K[x]$. And dually, as we have seen, the ring $\mathbb K[x]$ are the *(global) functions* on $\mathbb A_{\mathbb K}$.
# 
# 
# ```{note}
# 
# More formally still, $\mathbb K[x]$ are the global sections of the structure sheaf of $\mathbb K$-regular functions on $\mathbb A_{\mathbb K}$. But we don't need to get the mafia of sheaves involved in our business here.
# 
# ```
# 
# As a final remark, the space $\mathbb A_{\mathbb K}$ is one dimensional. The generalization to higher dimensions will proceed along lines one might expect. Affine spaces of dimension $n$, denoted $\mathbb A^n_{\mathbb K}$, are characterized *as* the spectrum of the polynomial ring $\mathbb K[x_1, \ldots, x_n]$.
# 

# ## The polynomial class
# 
# We will now describe and illustrate the methods in the polynomial class `Poly`, found in the module `polynomial.py`.
# 
# ### Library imports
# 
# While preparing this documentation, we store modules coding our function classes in the file `class_scripts`. Below is the appropriate library import of the module `polynomial.py`. It is only necessary for preparing these documents.

# In[1]:


from class_scripts import polynomial as pnml


# ### Class methods
# 
# The class `Poly` is coded in the module `polynomial.py`. Calling `help` on this class reveals all the methods available therein.

# In[2]:


help(pnml.Poly)


# ### Attributes and representation
# 
# 
# As mentioned earlier, polynomials are determined by properties of their coefficients. This justifies initializing any instance of the `Poly` by a tuple of coefficients $(a_0, \ldots, a_n)$. Any instance of `Poly` is, after all, a polynomial. When initialized, it has attributes `poly.coeffs` and `poly.degree`. These return the coefficients and the degree respectively of any instance of `Poly`.
# 
# To illustrate, consider the following polynomial
# 
# ```{math}
# 
# y = f(x) = 1 + 2x
# 
# ```
# 
# Its coefficients are $(1, 2)$. Passing this into `Poly` gives the polynomial object:

# In[3]:


poly = pnml.Poly([1, 2])
poly


# The instance `poly` has the following attributes:

# In[4]:


print(f"The coefficients defining {repr(poly)} are {poly.coeffs}")
print(f"The degree of {repr(poly)} is {poly.degree}")


# The method `coeff()` passes an integer `i` and returns the `i`-th coefficient. Concerning the above example:

# In[5]:


for i in range(poly.degree + 1):
    print(f"The {i}-th coefficient of {repr(poly)} is {poly.coeff(i)}")


# ```{note}
# 
# If the index `i` is outside the range of coefficients, the method `coeff()` does not raise an index error as one might expect. Instead it returns `None`.
# 
# ```

# Note here that `Poly([1, 2])` is the literal representation of an instance of `Poly`. The dunder `__str__` in `Poly` returns instances in a more human readable form, as follows:

# In[6]:


print(f"In more human readable form, {repr(poly)} is presented as: {poly}")


# The `__str__` method also allows for easy-to-read representation of negative signs. Consider the polynomials
# 
# $$
# \begin{align}
# g(x) 
# &= -2 + x - 4x^2;
# \\
# h(x)
# &= -x^2 + 2x^5
# \end{align}
# $$
# 
# These are printed as follows.

# In[7]:


poly_1 = pnml.Poly([-2, 1, -4])
poly_2 = pnml.Poly([0, 0, -1, 0, 0, 2])

print(f"g(x) is {poly_1}")
print(f"h(x) is {poly_2}")


# ```{warning}
# 
# Note that only tuples and lists are passable in `Poly`. Running `Poly(a)` for a scalar (number) `a` will accordingly result in a type error. In order to represent scalars as instances of `Poly` we need to pass the tuple `(a)` or list `[a]`. E.g., `Poly([1])` instead of `Poly(1)`.
# 
# ```
# 

# #### The zero polynomial
# 
# The zero polynomial `Poly([0])` is printed as `The zero polynomial`. Don't be fooled by the print statement however. It is still represented as an honest instance of `Poly`, as calling `repr` will illustrate. See the following code block.

# In[8]:


zero_poly = pnml.Poly([0])

print(zero_poly)
print(repr(zero_poly))


# #### Random instances of `Poly`
# 
# 
# With the class `Poly` defined, it is easy to generate random instances of `Poly`. Parameters to specify are: its degree and the range of possible values for its coefficients.
# 
# The following code draws on `random.randint` to generate integral polynomials.

# In[9]:


from random import randint

def generateNonzero(coeff_rng):
    num = randint(coeff_rng[0], coeff_rng[-1])
    if num != 0:
        return num
    else:
        return generateNonzero(coeff_rng)

def generatePoly(degree, coeff_rng):
    coeffs = []
    for _ in range(degree):
        coeffs += [randint(coeff_rng[0], coeff_rng[-1])]
        
    leading_coeff = generateNonzero(coeff_rng)
    coeffs += [leading_coeff]
    
    return pnml.Poly(coeffs)


# Utilizing the function `generateNonzero()` guarantees that the polynomial generated by `generatePoly()` will have the specified degree.
# 
# ```{note} 
# 
# In `generatePoly` we return `pnml.Poly` since the module `polynomial.py` is imported in this notebook as `pnml`. 
# 
# ```
# 
# The following is a list of six randomly generated, cubic polynomials whose coefficients are sampled from `-10` to `10`.

# In[10]:


degree = 3
coeff_rng = [-10, 10]

for _ in range(6):
    print(f"Random polynomial number {_}: {generatePoly(degree, coeff_rng)}")


# ### Further remarks
# 
# It is worth mentioning that in `__new__`, before initialising any `Poly` object, the coefficient list passed is checked for any trailing zeroes. Trailing zeroes are deleted. This is accordance with degree $n$ polynomials being polynomials whose $n$-th coefficient is *non-zero*. E.g., the polynoimal $1 + 0x$ has degree *zero*, not degree one. 
# 
# To illustrate, the following polynomial defined by coefficient list `[-1, 3, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0]` is reprsented and printed as:
# 

# In[11]:


print(f"in code format: {repr(pnml.Poly([-1, 3, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0]))}")
print(f"in more human readable format: {pnml.Poly([-1, 3, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0])}")
print(f"the length of the coefficient list is {len([-1, 3, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0])} but the polynomial degree is: {pnml.Poly([-1, 3, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0]).degree}")


# ## Arithmetic 
# 
# The set of polynomials over a field of scalars $\mathbb K$ forms a ring. This means we can add, subtract and multiply polynomials. We can also combine these operations with scalars since there is a ring embedding $i:\mathbb K \subset \mathbb K[x]$ given by $a \mapsto i(a)$, where $i(a)$ is the constant function:
# 
# ```{math}
# 
# (i(a))(x) = a.
# 
# ```
# 
# Recall the earlier warning that `Poly(a)` for any number `a` results in a type error. However, `Poly([a])` will return an instance of `Poly`. We can interpret `a` to be an element of $\mathbb K$ while `[a]` is its image $i(a)$ in $\mathbb K[x]$. 

# ### Evaluation
# 
# For any polynomial $f(x)$ and scalar $\lambda$, the evaluation function sends $f(x) \mapsto f(\lambda)$. The method  `eval()` on any instance of `Poly` playes the role of evaluation. To see this consider the polynomial,
# 
# ```{math}
# 
# f(x) = -1 + 5x + x^3 -7x^4 + 2x^6
# 
# ```
# 
# Evaluating $f$ at the scalar value `107` is implemented as follows:

# In[12]:


poly_to_eval = pnml.Poly([-1, 5, 0, 1, -7, 0, 2])
scalar = 107

print(poly_to_eval.eval(scalar))


# ### Implementation
# 
# In the class `Poly`, the dunders `__add__`, `__mul__`, `__sub__` and `__truediv__` allow for extending the familiar operators `+, *, -, /` to instances of `Poly`. 
# 
# ```{Note} 
# 
# The division `/` will not yield a rational function however, as the ratio of one polynomial to another is typically understood. It will instead perform polynomial long division (imported from Python's `numpy` library) and return the divisor and remainder as instances of `Poly`. In particular, it will return two instances of `Poly`. 
# 
# ```
# 
# To see these arithmetical operations implemented, consider the following two polynomials:
# 
# $$
# \begin{align}
# f(x) = 1 + x
# &&
# \mbox{and}
# &&
# g(x) = -1 + x.
# \end{align}
# $$
# 
# In what follows we will return:
# 
# - $f(x) + g(x)$
# - $f(x) - g(x)$
# - $f(x)\cdot g(x)$
# - $f(x)/g(x)$.

# In[13]:


poly_f = pnml.Poly([1, 1])
poly_g = pnml.Poly([-1, 1])

print(poly_f + poly_g)
print(poly_f - poly_g)
print(poly_f * poly_g)
print(poly_f / poly_g)


# #### The remainder theorem
# 
# Another characterisation of polynomial evaluation is by extracting a remainder. That is, in order to evaluate a polynomial $f(x)$ at a particular value $x = \lambda$, form the polynomial $g(x) = x - \lambda$, divide $f$ by $g$ and extract the remainder. The remainder of $f(x)/g(x)$ is precisely $f(\lambda)$. This result is referred to as the *Polynomial remainder theorem*. See [this Wikipedia article](https://en.wikipedia.org/wiki/Polynomial_remainder_theorem) for more details.
# 
# To see this in practice, recall that we evaluated the polynomial $f(x) = -1 + 5x + x^3 -7x^4 + 2x^6$ at $x = 107$ above, yielding the value `3000544372068`. We evaluated this by calling the `eval()` method, which in turn is coded as a direct computation. Via polynomial long division, we can calculate $f/(x - 107)$ and extract the remainder. 
# This is implemented in the following code block.

# In[14]:


poly_divide_by = pnml.Poly([-scalar, 1])
poly_division = poly_to_eval / poly_divide_by
remainder = poly_division[-1]

print(remainder)


# Recall that we set `scalar = 107` earlier. As expected, the remainder above coincides with `poly_to_eval.eval(scalar)`. 

# ### Powers
# 
# With multiplication between instances of `Poly` defined, it is straightforward to adapt `__pow__` to `Poly`, allowing for using `**`. To illustrate, the first five powers of $g(x) = -1 + x$ from above can be obtained as follows:

# In[15]:


for i in range(6):
    print(f"g(x) to the {i}-th power: {poly_g**i}")


# ### Polynomial composition
# 
# In the one dimensional case, polynomials can be unambiguously composed with one another. This is because, at the level of spaces, a polynomial $f$ over $\mathbb K$ is defines a morphism $\mathbb A_{\mathbb K} \stackrel{f}{\rightarrow} \mathbb A_{\mathbb K}$. Hence with two polynomials $f, g : \mathbb A_{\mathbb K} \rightarrow \mathbb A_{\mathbb K}$ it makes sense to form the composite $h = f\circ g$ where,
# 
# ```{math}
# 
# h: \mathbb A_{\mathbb K} \stackrel{g}{\longrightarrow} \mathbb A_{\mathbb K} \stackrel{f}{\longrightarrow} \mathbb A_{\mathbb K}.
# 
# ```
# 
# When represented in coordinates, if $f(x) = \sum_i a_ix^i$ and $g(x) = \sum_j b_j x^j$, then
# 
# ```{math}
# 
# h(x) = (f\circ g)(x) = \sum_i a_i (g(x))^i = \sum_{i, j} a_i b_j^ix^{i+j}.
# 
# ```
# 
# Note now, with `__mul__` and `__pow__` methods defined for the class `Poly`, code implementing the evaluation method `eval()` can be generalised straightforwardly to implement polynomial composition. This is done through the method `composeWith()` on any instance.
# 
# To illustrate, consider polynomials 
# 
# $$
# \begin{align}
# f(x) = 2x^2
# &&
# \mbox{and}
# && 
# g(x) = 1 + x^3
# \end{align}
# $$
# 
# The composition is,
# 
# ```{math}
# 
# h(x)
# =
# (f\circ g)(x)
# =
# 2(1 + x^3)^2
# =
# 2 + 4x^3 + 2x^6
# 
# ```
# 
# This is implemented in the class `Poly` as follows:

# In[16]:


first_poly_composite = pnml.Poly([0, 0, 2])
second_poly_composite = pnml.Poly([1, 0, 0, 1])

print(first_poly_composite.composeWith(second_poly_composite))


# ## Calculus 
# 
# ### Differentiation
# 
# A *monomial* is a particularly simple kind of polynomial - a polynomial with one term. Accordingly, any monomial in one variable is of the form
# 
# ```{math}
# 
# ax^i
# 
# ```
# 
# for scalar $a$ and degree $i$. Polynomials are, evidently, finite sums of monomials. Differentiation is a linear operator so in order to differentiate polynomials it suffices know how to differentiate monomials. An exercise in applying Newton's quotient definition of differentiation yields,
# 
# ```{math}
# 
# \frac{d}{dx} (ax^i) = iax^{i-1}.
# 
# ```
# 
# Observe that the derivative of a monomial is again a monimial. Hence, the derivative of polynomials are polynomials. This justifies implementing differentiation as a method in the class `Poly`. It is implemented as `diff()`. For the following polynomial,
# 
# ```{math}
# 
# f(x) = -3 + 4x^2 + x^5
# 
# ```
# 
# its derivative is:

# In[17]:


poly_to_diff = pnml.Poly([-3, 0, 4, 0, 0, 1])

print(poly_to_diff.diff())


# #### Higher order differentiation
# 
# Differentiation preserves the class of polynomials, in the sense that the derivative operator on a polynomial returns a polynomial. As such it makes sense to use `diff()` to recursively define differeniation to any specified order. In `Poly` this is implemented as the method `Hdiff()` which passes an integer $n$ and returns the $n$-order derivative operator $d^n/dx^n$. 
# 
# On the polynomial $f(x) = -3 + 4x^2 + x^5$ we can readily print derivatives of any order. Derivatives of $f(x)$ up to $7$-th order are:

# In[18]:


for i in range(7 + 1):
    print(f"The {i}-th derivative of {poly_to_diff} is: {poly_to_diff.Hdiff(i)}")


# ### Integration
# 
# Like differentiation, (indefinite) integration of monomials are monimials. For the monimial $ax^i$,
# 
# ```{math}
# 
# \int ax^idx
# =
# \frac{a}{i+1}x^{i+1}.
# 
# ```
# 
# By linearity then, integration of polynomials are polynomials. Integration is implemented by the `intgr()` method in `Poly`. For the following polynomial,
# 
# ```{math}
# 
# f(x) = 5 - 3 x^4
# 
# ```
# 
# its integral is implemented as follows:

# In[19]:


to_intgr = pnml.Poly([5, 0, 0, 0, -3])

print(f"The (indefinite) integral of {to_intgr} is: {to_intgr.intgr()}")


# The derivative of the integral of a function is the original function. And so as a consistency check on our integrated function $f(x)$:

# In[20]:


integrated = to_intgr.intgr()

print(f"The derivative of the integral of {to_intgr} is: {integrated.diff()}")


# #### Higher order integration
# 
# Since integration returns polynomials, it is possible to iteratively define integration of any order, much like differentiation. Higher order integration is implemented through the method `Hintgr()`. This method passes in an integer and returns an integral to that order.
# 
# On our function $f(x) = 5 - 3x^4$ above, its integral to $5$ orders is implemented and printed below:

# In[21]:


for i in range(6):
    print(f"The integral of {to_intgr} to {i}-th order is: {to_intgr.Hintgr(i)}")


# ```{note}
# 
# Inspection of `__str__` shows, in the print statement, that the coefficients are printed to four significant figures. To change this, change the entry `sig_figures` accordingly.
# 
# ```

# #### Area under the curve
# 
# The fundamental theorem of calculus for functions of one variable states: that for an integrable function $f(x)$ and a range $[a, b]$,
# 
# ```{math}
# 
# \int_{[a, b]} f(x)dx = (\int f(x)dx)(b) - (\int f(x) dx)(a)
# 
# ```
# 
# where $\int f(x) dx$ is the indefinite integral of $f$. Calling the method `AreaUnder()` on any `Poly` instance and passing in a range `[a, b]` returns the area bounded by the polynomial $f(x)$, the $x$-axis and vertical lines at $x = a$ and $a = b$.
# 
# To illustrate, the area under $f(x) = 3x^4$ between the range $[-1, 4]$ is:

# In[22]:


poly_area = pnml.Poly([0, 0, 0, 0, 3])

print(poly_area.AreaUnder([-1, 4]))


# ## Greatest common divisor
# 
# 
# ### Background 
# 
# As with integers, for two polynomials $f, g$ there is always a common divisor, namely the unit polynomial $1$. In further similarity, it is possible to find larger common divisors. Recall that a polynomial $h$ *divides* $f$ if, in the polynomial long division $f/h$, the remainder is the zero polynomial. Euclid's famous algorithm for finding the greatest common divisor for two integers can be adapted straightforwardly for finding the greatest common divisor for two univariate polynomials. 
# 
# We decribe the algorithm in what follows. Let $f, g$ be two univariate polynomials. Suppose that $\deg f \geq \deg g$. Then the polynomial long division states that there exist polynomials $(f_1, f_2)$ such that 
# 
# ```{math}
# 
# f = gf_1 + f_2
# 
# ```
# 
# with $\deg f_2 < \deg g$. Here $f_2$ is the remainder in the division $f/g$. 
# 
# Remember, we want to find the greatest *common* divisor of $f, g$ which means a polynomial $h$ which divides both $f$ and $g$. Now, in the case $f_2 = 0$ above, the remainder of $f/g$ is zero. Hence $f = gf_1$. Since $f_1$ is polynomial, it follows that $f$ is divisible by $g$. Now, $g$ is also divisible by $g$ so therefore the greatest common divisor will be the denominator $g$.
# 
# In the case $f_2$ is *not* the zero polynomial, we need to check divisibility for $g$. Now in order for $f$ and $g$ to have a common divisor, note that it is equivalent for $g$ and $f_2$ to have a common divisor. Since $\deg f_2 < \deg g$ we can divide $g$ by $f_2$ to get the next relation,
# 
# ```{math}
# 
# g = f_2 g_1 + g_2
# 
# ```
# 
# with $g_2$ the remainder of $g/f_2$. If $g_2$ now is the zero polynomial, we find that $g$ is divisible by $f_2$. Consequently, with $f = gf_1 + f_2$, this means $f$ will also be divisible by $f_2$. Hence that $f_2$ will be the greatest common divisor.
# 
# If $g_2$ is *not* the zero polynomial, we can repeat this process now for the pair of remainders $f_2, g_2$ noting that $\gcd(f, g) = \gcd(f_2, g_2)$.
# 
# ```{note}
# 
# This algorithm will terminate since the degrees of $f_2, g_2$ are less than the original polynomials $f, g$. That is, with $\deg g \leq \deg f$ we will eventually arrive at a base case, which is the case where $g$ is a linear form (a polynomial of degree *one*). 
# 
# ```
# 
# ### Implementation
# 
# Euclid's algoritm for finding the greatest common divisor of two polynomial is callable through the method `gcd()` on any instance of `Poly`. As an illustration, let $f(x) = 1 + 2x + x^2$ and $g(x) = x+1$. Their greatest common divisor is then:

# In[23]:


find_divisor_1 = pnml.Poly([1, 2, 1])
find_divisor_2 = pnml.Poly([1, 1,])

print(find_divisor_1.gcd(find_divisor_2))


# Indeed, in this example $f(x) = 1 + 2x + x^2 = (1 + x)^2$.

# In[ ]:




