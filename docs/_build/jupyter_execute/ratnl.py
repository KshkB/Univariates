#!/usr/bin/env python
# coding: utf-8

# # Rational functions (basics)
# 
# Any polynomial is a rational function but not conversely. A *rational function* in one variable is a the ratio of one polynomial to another. Any rational function $R(x)$ can be expressed as 
# 
# ```{math}
# 
# R(x)
# =
# \frac{f(x)}{g(x)}
# 
# ```
# 
# for polynomials $f(x), g(x)$. 
# 
# Many of the properties for polynomials adapt straightforwardly to rational functions, albeit with minor changes. Furthemore, many operations for rational functions can be expressed in terms of operations on polynomials. For instance, arithmetical operations such as addition and multiplication can expressed in terms of those operations on  polynomials. For rational functions $R(x), S(x)$ given by polynomials,
# 
# $$
# \begin{align}
# R(x)
# =
# \frac{f(x)}{g(x)}
# &&
# \mbox{and}
# &&
# S(x) 
# =
# \frac{h(x)}{i(x)}
# \end{align}
# $$
# 
# we have
# 
# $$
# \begin{align}
# R(x) + S(x)
# &= 
# \frac{f(x) i(x) + g(x) h(x)}{g(x) i(x)};
# \\
# R(x)\cdot S(x)
# &=
# \frac{f(x)\cdot h(x)}{g(x)\cdot i(x)}.
# \end{align}
# $$
# 
# See that on the left hand side, addition and multiplication is for rational functions. On the right hand side instances of addition and multiplication are for polynomials.
# 
# ## Mathematical background
# 
# Recall that the ring of polynomials over a field $\mathbb K$ are dual to affine $\mathbb K$ space $\mathbb A_{\mathbb K}$. That is, the affine space $\mathbb A_{\mathbb K}$ can be understood as the spectrum of the ring $\mathbb K[x]$. Does there exist an analogous interpretation for rational functions? 
# 
# Firstly, as arithmetical operations make sense for rational functions, the set of rational functions in one variable also forms a ring (in fact, it forms a *field* in much the same way that the rational numbers $\mathbb Q$ is a field obtained from the integers $\mathbb Z$, which is only a ring). Moreover, as any polynomial is a rational, the set of polynomials is *contained* in that of rationals. More strongly, as we have seen above, arithematical operations for rationals can be expressed interms of operations on polynomials. It follows that containment of polynomials in rationals goes beyond simply an inclusion of sets. We have in fact an inclusion of *rings*. 
# 
# To phrase this symbolically, recall that $\mathbb K[x]$ denotes the ring of polynomials in one variable. Let $\mathbb K(x)$ denote the ring of rational functions in one variable. Then there exists an *embedding as rings* $\iota: \mathbb K[x]\subset \mathbb K(x)$. What we want to know however is whether there is a geometric interpretation for $\mathbb K(x)$ in analogy to that for $\mathbb K[x]$? That is, is there some topological space $X$ which can be realised as the spectrum of $\mathbb K(x)$? 
# 
# Generically, for the set of *all* rational functions in one variable, there is no such *affine* space. The main issue lies in the domains of definition. For a given rational function $R(x)$, it will not be defined at values of $x$ which are roots of the denominator. Hence, in contrast to polynomials, different rational functions will have different domains of definition, c.f., $R(x) = 1/x$ and $S(x) = 1/(x-1)$. 
# 
# In order to arrive at a geometric understanding of rational functions, it is necessary to consider the notion of "partial functions" on *projective spaces*. 
# 
# To stay within the realm of affine spaces, if a particular denominator polynomial is specified, then the locus of points at which it does *not* vanish defines an open subspace of affine space. This in fact characterizes *all* affine subspaces (known as "affine subvarieties"). And so, if $D\subset \mathbb A_{\mathbb K}$ is a domain at which $g(x) = 0$ for all $x \in D$, then the ring of *functions on $D$* is the ring of remainders $\mathbb K[x]/(g(x))$, i.e., $D$ is the spectrum of $\mathbb K[x]/(g(x))$. 
# 
# ```{note}
# 
# In the one dimensional case, $D$ will just be a finite collection of points which are roots of $g(x)$. Indeed, recall that the Polynomial Remainder Theorem gives an interpretation of polynomial evaluation via polynomial division. For a polynomial $f(x)$ and value $\lambda$, $f(\lambda)$ is the remainder of $f(x)/(x-\lambda)$. Here $g(x) = x - \lambda$ is a polynomial with root $x = \lambda$. Note therefore that *any* polynomial $f(x)$ which vanishes at $\lambda$ is necessarily a multiple of $g(x)$. Hence, any function $f$ which is *not* equal to a multiple of $g(x)$ will be a *non-zero* function on the singleton point $D = \{\lambda\}\subset \mathbb A_{\mathbb K}$. 
# 
# Written another way, if $\mathbb K[D] = \mathbb K[\{\lambda\}]$ denotes the ring of functions on the singleton $D = \{\lambda\}$, then 
# 
# $$
# \mathbb K[D] = \mathbb K[\{\lambda\}] = \frac{\mathbb K[x]}{(x-\lambda)}.
# $$
# 
# 
# ```
# 
# 
# 

# ## The Rational class
# 
# A class for rational functions is coded in the module `rational.py` as `Rational`. Since operations on rational functions can be expressed through polynomials, it is convenient to draw on methods from the class `Poly` in `polynomial.py`. 
# 
# ```{note}
# 
# This does *not* mean `Rational` is a subclass of `Poly`. It does not inherit all the same attributes. 
# 
# ```
# 
# ### Library import
# 
# The module coding for the class of rational functions is `rational.py`. Below is the appropriate library import for 
# preparing this document.

# In[1]:


from class_scripts import rational as rtnl


# ## Attributes and representation
# 
# Many of the methods and attributes in `Poly` adapt to `Rational`. While in `Poly` we need only remember one polynomial, in `Rational` two polynomials are stored with an indication of which is the numerator and which the denominator.  
# 
# For the rational function
# 
# ```{math}
# 
# R(x)
# = 
# \frac{1}{x^2}
# 
# ```
# 
# it is represented as:

# In[2]:


rat_1 = rtnl.Rational([1], [0, 0, 1])
print(repr(rat_1))


# The above print statement has returned the a statement in machine readable format. In more human readable format we have, as with `Poly`:

# In[3]:


print(rat_1)


# Evidently, an instance of `Rational` consists of two instances of `Poly`. Attributes stored for `Rational` are the attributes of the defining polynomial instances. These are called as follows. 

# In[4]:


print(rat_1.numerator)
print(rat_1.numdeg)
print(rat_1.denominator)
print(rat_1.denomdeg)


# ## Arithmetic
# 
# ### Evaluation
# 
# Unlike for polynomials, rational functions are not necessarily defined for any argument values. The method `eval()` takes this into account and returns a value if it exists or returns `Undefined` if it does not. For the above rational function $R(x) = 1/x^2$, it is defined for all $x \in \{x:x\neq0\}$. 
# 
# At values $x = 1$ and $x = 0$ respectively we have:

# In[5]:


val_1 = 1
val_2 = 0

print(rat_1.eval(1))
print(rat_1.eval(0))


# ### Implementation
# 
# As with instances of `Poly` we can adapt addition, subtraction, multiplication and division to `Rational`. To illustrate, for rational functions
# 
# $$
# \begin{align}
# R(x) = \frac{1}{x^2}
# &&
# \mbox{and}
# &&
# S(x) = \frac{-1 + x^2}{x}
# \end{align}
# $$
# 
# we will return:
# 
# - $R(x) + S(x)$;
# - $R(x) - S(x)$;
# - $R(x) \cdot S(x)$;
# - $R(x)/S(x)$.

# In[6]:


rat_R = rtnl.Rational([1], [0, 0, 1])
rat_S = rtnl.Rational([-1, 0, 1], [0, 1])

print(f"{rat_R + rat_S}\n")
print(f"{rat_R - rat_S}\n")
print(f"{rat_R * rat_S}\n")
print(f"{rat_R / rat_S}\n")


# ````{note}
# 
# The division method `__truediv__` does not perform any polynomial division as with instances of `Poly`. For rational functions $R = f/g$ and $S = h/i$, the division operator `/` returns for `R/S` the formal division,
# 
# ```{math}
# 
# \frac{R}{S} = \frac{f}{g}\cdot \frac{i}{h}.
# 
# ```
# 
# ````
# 
# In this way, division of two rational functions returns a rational function.

# ### Powers
# 
# From the `__mul__` method we can define `__pow__` implementing powers of rational functions. For the rational $R(x) = \frac{1}{x^2}$, its first five powers are:

# In[7]:


for i in range(5+1):
    print(f"The {i}-th power of {repr(rat_R)} is:\n{rat_R**i}\n")
    


# ### Composition
# 
# Formally, we might think of rational functions as mappings $\mathbb A_{\mathbb K} \rightarrow \mathbb A_{\mathbb K}$. In particular, it makes sense to compose them as in the case of polynomials. For rationals $R(x), S(x)$,
# 
# ```{math}
# 
# T(x) = (R\circ S)(x) = R(S(x)) = \frac{f(S(x))}{g(S(x))}
# 
# ```
# 
# With $R(x) = 1/x^2$ and $S(x) = (-1 + x^2)/x$, 
# 
# ```{math}
# 
# T(x)
# =
# \frac{1}{S(x)^2}
# =
# \frac{x^2}{(-1 + x^2)^2}
# 
# ```
# 
# We can call the method `composeWith()` to implement composition:

# In[8]:


print(rat_R.composeWith(rat_S))


# ```{note}
# 
# We have not simplified the above expressions. We will come to simplification shortly. 
# 
# ```

# ## Differentiation
# 
# As with the arithmetic, differentiation of rational functions can be expressed through differentiation of polynomials. For $R(x) = f(x)/g(x)$ the quotient polynomials $f$ and $g$, its derivative is
# 
# ```{math}
# 
# \frac{d}{dx}R(x)
# =
# \frac{\left(\frac{d}{dx}f\right)\cdot g(x) - f(x)\cdot \left(\frac{d}{dx}g\right)}{g(x)^2}
# 
# ```
# 
# On the left-hand side is the derivative of rational function $R(x)$; while on the right-hand we find derivatives of polynomials. The method `diff()` passes no arguments and returns the derivative of an instance of `Rational`.
# 
# ```{note}
# 
# As with polynomials, the derivative of a rational function is again rational. Differentiation therefore preserves instances of the class `Rational`.
# 
# ```
# 
# As an illustration, for $R(x) = 1/x^2$, its derivative is:

# In[9]:


print(rat_R.diff())


# #### Higher order differentiation
# 
# The method `Hdiff()` passes in an integer and returns the $n$-th order derivative $d^n/dx^n$. The first five derivatives of $R(x)$ are:

# In[10]:


for i in range(5+1):
    print(f"The {i}-th derivative of {repr(rat_R)} is:\n{rat_R.Hdiff(i)}\n")


# Unlike for polynomials, it is a more subtle issue to integrate rational functions. While there is a general formula, it involves analytic functions of complex variables. In particlar it is *not* a rational function.

# ## Simplification
# 
# 
# If two integers $m, n$ share a common multiple $p$, then $m/n = (m/p)/(n/p)$. Similarly, for any rational function $R = f/g$ and any common divisor $h$
# 
# ```{math}
# 
# R = \frac{f}{g} = \frac{f/h}{g/h}.
# 
# ```
# 
# In this way, rational functions can be simplified by simultaneously reducing the degrees of the numerator and denominator. For example, with $f(x) = x^3$ and $g(x) = x^7$, 
# 
# ```{math}
# 
# R(x) = \frac{f(x)}{g(x)} = \frac{x^3}{x^7} = \frac{1}{x^4}.
# 
# ```
# 
# ### Implementation
# 
# Recall that the class `Poly` contains the method `gcd()` which passes in two instances $f, g$ and returns their greatest common divisor. This forms the basis for the method `simply()`, callable on any instance of `Rational`. 
# 
# To illustrate, the following rational function:
# 
# ```{math}
# 
# \frac{-1 + x^2}{1 + x}
# 
# ```
# 
# simplifies to:

# In[11]:


to_simplify = rtnl.Rational([-1, 0, 1], [1, 1])
print(to_simplify.simplify())


# This is indeed the correct simplification upon noting $-1 + x^2 = (1 + x)(1-x)$. On dividing through by $1+x$ we obtain the rational function $\frac{-1 + x}{1}$.

# In[ ]:




