#!/usr/bin/env python
# coding: utf-8

# # The cubics
# 
# Polynomials of degree three are referred to as *cubics*. In one variable, cubic univariates. They are generically of the form 
# 
# ```{math}
# 
# f(x) = d + cx + bx^2 + ax^3
# 
# ```
# 
# for $a\neq0$. As with the quadratics, cubic polynomials are polynomials. They are coded in the module `cubics.py` as a subclass of `Poly`. 
# 
# ## Library import

# In[1]:


from class_scripts import cubics as cbc


# ## Attributes
# 
# ### Pre-initialisation
# 
# The `__new__` method is run before initialisation and verifies whether a given array is indeed a member of the class `Cubic`. Recall, it will be a cubic if it has degree *three* with non-zero leading term. The following two instances are *not cubic*, as detected by `__new__`.

# In[2]:


cbc_test_1 = cbc.Cubic([1])
cbc_test_2 = cbc.Cubic([-4, 5, -2, 0])
cbc_test_3 = cbc.Cubic([-3, 3, 1, -4, 0])

print(cbc_test_1)
print(cbc_test_2)
print(cbc_test_3)


# ### Initialisation
# 
# For an honest cubic $f(x) = d + cx + bx^2 + ax^3$, it comes with all the attributes of `Poly`. Furthermore, as with quadratics, it is much faster to calculate its discriminant from the coefficients passed rather than first calculating its resultant.
# 
# To illustrate, on the cubic $f(x) = -3 + 5x + x^2 -12x^3$, when initialised it has attribues:

# In[3]:


cbc_1 = cbc.Cubic([-3, 5, 1, -12])

print(f"The cubic polynomials is: {cbc_1}")
print(f"Its coefficient list is: {cbc_1.coeffs}")
print(f"The degree of the cubic is: {cbc_1.degree}")
print(f"Its discriminant is: {cbc_1.disc}")


# As a check, to see that its discriminant coincides with the discrinimant call `discriminant()` when viewed as an instance of `Poly`, see that:

# In[4]:


print(cbc_1.discriminant())


# ## Cubic depression
# 
# ### Preliminaries
# 
# An important transformation for cubics is the *depression*. A *depressed cubic* $g(x)$ is a cubic of the form $g(x) = q + px + x^3$ for coefficients $p, q$. From the [Wikipedia entry](https://en.wikipedia.org/wiki/Cubic_equation#Depressed_cubic), *any* cubic can be transformed into depressed form. 
# 
# For a general cubic $f(x) = d + cx + bx^2 + ax^3$, recall that we know $a\neq0$. As such we can divide through by the leading coefficient $a$ without cause for heart palpatations. The transformation $x \mapsto x - \frac{b}{3a}$ will send $f$ to the form $\tilde f(x) = aq + apx + ax^3$. Dividing through by $a$ gives the depressed cubic $g(x) = q + px + x^3$. The new coefficients $(p, q)$ can be expressed in terms of the old coefficients $(a, b, c, d)$ thusly,
# 
# $$
# \begin{align}
# p
# =
# \frac{3ac - b^2}{3a^2}
# &&
# \mbox{and}
# &&
# q 
# =
# \frac{2b^3 - 9abc + 27 a^2d}{27 a^3}.
# \end{align}
# $$
# 
# ### Implementation
# 
# In the class `Cubic`, the method `toDepressed()` takes any instance of `Cubic` and, through the above formula for the coefficients, returns its depression which is another instance of `Cubic`. To illustrate, consider the cubic,
# 
# ```{math}
# 
# f(x) = 1 + 7x - 3x^3 + 2x^3
# 
# ```
# 
# Its depression is:

# In[5]:


undepressed = cbc.Cubic([1, 7, -3, 2])
print(undepressed.toDepressed())


# We obtained the above cubic by applying the formula. It is also possible to recover it through composing it with the transformation $x \mapsto x - \frac{b}{3a}$ and dividing the resulting polynomial by $a$. This can be implemented through the `composeWith()` method callable on any instance of `Poly`. In doing so:

# In[6]:


leading_coeff = undepressed.coeff(undepressed.degree)
coeff_b = undepressed.coeff(undepressed.degree - 1)

composite = cbc.Poly([-coeff_b/(3*leading_coeff), 1])
factor = cbc.Poly([1/leading_coeff])


print(factor * undepressed.composeWith(composite))


# ## Zeroes
# 
# ### Background 
# 
# A *root* of a cubic univariate $f(x) = d + cx + bx^2 + ax^3$ is a value $x_0$ such that 
# 
# ```{math}
# 
# f(x_0) = 0.
# 
# ```
# 
# The problem of expressing roots of a cubic univariate in terms of its coefficients and radicals, in a manner analogous to the case of quadratic univariates, is a classical problem in the history of mathematics. Over the complex numbers, there will always exist three roots of $f$, counted with multiplicity. 
# 
# #### Utility of depression
# 
# Recall that any cubic can be transformed into a much simpler cubic, name its depression. The problem of finding roots of the cubic can therefore be reduced to finding roots of its depression, which is significantly easier. Since we know the transformation $x \mapsto x - \frac{b}{3a}$ sends the original cubic $f$ to (a multiple of) its depressed form, we can therefore obtain the root of $f$ by simply translating back any root of its depressed form. More explicitly, if $x_{depr}$ is a root of the depressed form of $f$, then the translate $x_{depr} + \frac{b}{3a}$ will be a root of $f$.
# 
# For any (real) depressed cubic $g(x) = q + px + x^3$ with *negative discriminant* Cardano famously obtained a formula for one of the roots in terms of the coefficients $p, q$ and their radicals (specifically, square- and cube-roots). 
# 
# ```{note}
# 
# Recall that it suffices to find only one root. The others can be obtained on multiplying by an appropriate root of unity. Once we have three roots we know, by the fundamental theorem of algebra, that we have found *all* the roots. With Cardano's formula and a cube root of unity it is possible to derive all the roots of a cubic.
# 
# ```
# 
# See [this Wikipedia entry](https://en.wikipedia.org/wiki/Cubic_equation#General_cubic_formula) for the general formula for roots of a cubic.
# 
# ```{note}
# 
# The formula from the above entry is valid in the same generality as in the quadratic case, i.e., for *complex* cubics, not just real cubics.
# 
# ```
# 
# ### Implementation
# 
# The method `zeroes()` is callable on instances of the class `Cubic`. When called on an instance it returns a list of its zeroes. To illustrate, for the following cubics:
# 
# - $-10 + x + 5x^3$;
# - $x -9x^2 + x^3$;
# - $-34 + 6x^2 + 2x^3$;
# - $1 + x + x^2 + x^3$
# 
# Their zeroes are:
# 

# In[7]:


test_cubic_1 = cbc.Cubic([-10, 1, 0, 5])
test_cubic_2 = cbc.Cubic([0, 1, -9, 1])
test_cubic_3 = cbc.Cubic([-34, 0, 6, 2])
test_cubic_4 = cbc.Cubic([1, 1, 1, 1])

test_cubics = [test_cubic_1, test_cubic_2, test_cubic_3, test_cubic_4]

for c in test_cubics:
    print(f"Zeroes of {c} are:")
    c_zros = c.zeroes()
    print(*c_zros, sep='\n')
    print('\n')    


# The value of the cubic at each zero must of course be zero. 
# 
# 
# 
# And so, as a sanity check on the method `zeroes()` we need to check, for each cubic in `test_cubics` above, that the cubic at that value is indeed zero. As the method `zeroes()` returns complex numbers, i.e., instances of `cplx`, to evaluate a polynomial thereon requires calling `cplxEval()` from `Poly`. We find:

# In[8]:


for c in test_cubics:
    c_zros = c.zeroes()
    for zro in c_zros:
        print(c.cplxEval(zro))
    print('\n')


# And so for each cubic in `test_cubics`, each of their zeroes indeed returns zero upon evaluation, as expected.

# In[ ]:




