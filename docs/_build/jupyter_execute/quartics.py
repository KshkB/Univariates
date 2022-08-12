#!/usr/bin/env python
# coding: utf-8

# # Quartics
# 
# In degree four we find the quartics. In one variable, any quartic univariate $f(x)$ is given by
# 
# ```{math}
# 
# f(x) = e + dx + cx^2 + bx^3 + ax^4
# 
# ```
# 
# for $a\neq0$. Quartics are coded in `quartics.py` under the class `Quartic`, which is a subclass of `Poly`. That is, quartics are instances of `Quartic`. As quartics are also polynomials, they will be instances of `Poly`.
# 

# ## Library import
# 

# In[1]:


from class_scripts import quartic as qrtc


# ## Attributes
# 
# ### Pre-initialisation
# 
# As with quadratics and cubics, quartics are polynomials of degree $4$ with *non-zero* leading coefficient. This is detected by the `__new__` method which runs before initialising any instance. 
# 
# The following are examples of polynomials which are *not* quartic.

# In[2]:


not_quart_1 = qrtc.Quartic([1, 5, -2, 10])
not_quart_2 = qrtc.Quartic([-3, 4, 1, 2, 0])
not_quart_3 = qrtc.Quartic([-1, 7, 3, -8, 1, 1])


print(not_quart_1)
print(not_quart_2)
print(not_quart_3)


# ### Initialisation
# 
# For an honest quartic $f(x) = e + dx + cx^2 + bx^3 + ax^4$, all of its attributes are inherited from the class `Poly`. For example, for 
# 
# ```{math}
# 
# f(x) = -1 + x + 3x^2 - 9x^3 + 2x^4
# 
# ```
# 
# its attributes are:

# In[3]:


quart = qrtc.Quartic([-1, 1, 3, -9, 2])

print(f"The degree of {quart} is: {quart.degree}")
print(f"The coefficients defining {quart} is: {quart.coeffs}")


# Unlike for the quadratic and cubic, the discriminant of a quartic is not coded as an attribute of `Quartic`. It must be obtained instead by calling the method `discriminant()`. For the quartic above:

# In[4]:


print(f"The discriminant if {quart} is: {quart.discriminant()}")


# ## Depression
# 
# As with the cubic, it is always possible to transform a quartic to "depressed" form. A *depressed quartic* is a quartic $g(x)$ of the form,
# 
# ```{math}
# 
# g(x) = \gamma + \beta x + \alpha x^2 + x^4
# 
# ```
# 
# With $f(x) = e + dx + cx^2 + bx^3 + ax^4$, if can be placed in depressed form through the variable change $x \mapsto x - \frac{b}{4a}$, followed by dividing through the leading coefficient $a$. See [this Wikipedia entry](https://en.wikipedia.org/wiki/Quartic_equation#Converting_to_a_depressed_quartic) for the formula relating the coefficients of $f$ with those of $g$. 
# 
# ### Implementation
# 
# The formula relating the coefficients of a quartic to its depressed form is implemented by the method `toDepressed()`. Recall, the same method is callable on instances of `Cubic`. This method passes in quartics and returns their depressed form using the formula from the above Wikipedia entry.
# 
# As an illustration, for the quartic $f(x) = -1 + x + 3x^2 - 9x^3 + 2x^4$ from above, its depression is:
# 

# In[5]:


depr_quart = quart.toDepressed()
print(depr_quart)


# Recall that depression can also be derived through variable change. And so to check the validity of the formula implemented in `toDepressed()`, we can compose $f(x)$ with the polynomial $x - b/4a$ and divide through by $a$. Doing this we find:

# In[6]:


a = quart.coeff(quart.degree)
b = quart.coeff(quart.degree-1)

composite = qrtc.Poly([-b/(4*a), 1])
quart_composed = quart.composeWith(composite)
quart_depressed = quart_composed * qrtc.Poly([1/a])

print(quart_depressed)


# This validates the formula used in the method `toDepressed()`.

# ## Zeroes
# 
# ### Background 
# 
# For a quartic univariate $f(x) = e + dx + cx^2 + bx^3 + ax^4$, a zero is a value $x_0$ such that $f(x_0) = 0$. The quartics are the highest degree polynomials for which an algebraic formula exists for their zeroes. That is, a formula involving only algebraic expressions of the coefficients. 
# 
# ```{note}
# 
# It is known that in degrees *five* and higher, no such algebraic formula exists for returning roots. 
# 
# ```
# 
# As with cubics, the method for deriving the formula for quartic roots involves first depressing the quartic. The attentive reader might note however that the module `quartic.py` imports `quadratic.py` and `cubic.py`. This is because any formula for the roots of a quartic involve solving a cubic equation. From [this entry](https://en.wikipedia.org/wiki/Quartic_equation#Solving_a_depressed_quartic_when_b%E2%89%A00) a formula for the roots of a general quartic (in depressed form), $f(x) =  c + bx + ax^2 + x^4$, for $a, b$ non-zero, can be expressed via any solution of the following cubic equation (in variable $y$),
# 
# ```{math}
# 
# \left(ac - \frac{1}{4}b^2\right) - 2cy - ay^2 + 2y^3 = 0
# 
# ```
# 
# In a degenerate case $b = 0$, the depressed quartic can be solved using the quadratic equation.
# 
# ### Implementation
# 
# The method `zeroes()` is callable on any instance of the class `Quartic`. It passes in any instance of `Quartic` and returns a list of its zeros. 
# 
# To illustrate, for the following quartics:
# 
# - $-12 + 3 x + 2x^4$;
# - $3 - x + 7x^2 + 5x^3 - 7x^4$;
# - $8 + 2x^2 + 3x^4$
# 
# their zeroes are:
# 

# In[7]:


qt_1 = qrtc.Quartic([-12, 3, 0, 0, 2])
qt_2 = qrtc.Quartic([3, -1, 7, 5, -7])
qt_3 = qrtc.Quartic([8, 0, 2, 0, 3])

qt_list = [qt_1, qt_2, qt_3]

for qt in qt_list:
    print(*qt.zeroes(), sep='\n')
    print('\n')


# As a check now that we have indeed returned zeroes, we run the following:

# In[8]:


for qt in qt_list:
    zros = qt.zeroes()
    for zro in zros:
        print(qt.cplxEval(zro))
    print('\n')
    


# We find that the quartic evaluated at each zero indeed returns zero, as expected.

# In[ ]:




