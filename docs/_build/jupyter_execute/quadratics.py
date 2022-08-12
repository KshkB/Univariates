#!/usr/bin/env python
# coding: utf-8

# # Quadratic univariates
# 
# Quadratic polynomials are polynomials of degree *two*. If the polynomials are in one variable, they are univariate polynomials. Quadratic univariate polynomials are therefore polynomials in one variable of degree *two*. These are referred to simply as quadratic univariates. 
# 
# ```{note}
# 
# A quadratic might also refer to a *homogeneous* polynomial of degree two. In this document, by quadratic it is  meant a not-necessarily-homogeneous, degree two polynomial. 
# 
# ```
# 
# Any quadratic univariate $f(x)$ is of the form
# 
# ```{math}
# 
# f(x) = c + bx + ax^2
# 
# ```
# 
# for coefficients $(a, b, c)$. As quadratic univariates are univariate polynomials, it makes sense to form the class of quadratic univariates as a subclass of polynomials.
# 
# ## Library import
# 
# In the module `quadratics` we find the class `Quadratic` coded as a subclass of `Poly`. Below is the libary import.

# In[1]:


from class_scripts import quadratics as qd


# ## Attributes
# 
# ### Pre-initialisation
# 
# As with `Poly` the class `Quadratic`, being a subclass of `Poly`, has the same attributes. Importantly however, if we pass an array encoding a polynomial with does *not* have degree two, it is not quadratic and this is detected by `__new__`. 
# 
# To illustrate, if we pass the arrays `[1, 2]` and `[-3, 2, 4, 1]` which encode the polynomials $1 + 2x$ and $-3 + 2x + 4x^2 + x^3$ the class `Quadratic` returns:
# 

# In[2]:


print(qd.Quadratic([1, 2]))
print(qd.Quadratic([-3, 2, 4, 1]))


# Similarly, if we pass `[1, 2, 0]`, this array encodes $1 + 2x + 0x^2$. The class `Quadratic` will nevertheless return:

# In[3]:


print(qd.Quadratic([1, 2, 0]))


# Attempting to then return an attribute will result in an attribute error. 
# 
# ### Initialisation
# 
# For an honest quadratic $f(x) = c + bx + ax^2$, it has all the attributes and methods callable on instances of `Poly`. Moreover, it has its discriminant $b^2 - 4ac$ as an attribute.
# 
# ```{note}
# 
# It is of course possible to call `discriminant()` on an instance of `Quadratic`. This involves forming the derivative, the Sylvester matrix, taking its determinant and multiplying by an appropriate factor. If a  polynomial function of the coefficients is already known, it is much faster to form this instead. This is what is formed by the attribute `disc`.
# 
# ```
# 
# 
# To illustrate, for the quadratic $f(x) = -9 + x + 4x^2$ its attributes are:

# In[4]:


quad_f = qd.Quadratic([-9, 1, 4])

print(f"The polynomial is: {quad_f}")
print(f"Its coefficient list is: {quad_f.coeffs}")
print(f"Its degree is: {quad_f.degree}")
print(f"Its discriminant is: {quad_f.disc}")


# As a quick test, to see that the `discriminant()` method called on `quad_f` as an instance of `Poly` will agree with `quad_f.disc` above, we have:

# In[5]:


print(quad_f.discriminant())


# ## Zeroes
# 
# For a quadratic univariate $f(x) = c + bx + ax^2$, $x_0$ is a zero of $f(x)$ if:
# 
# ```{math}
# 
# c + bx_0 + ax_0^2 = 0.
# 
# ```
# 
# From the fundamental theorem of algebra, $f$ has degree two so it has two zeroes $x_1, x_2\in \mathbb C$. Since the real numbers are not algebraically closed, $f$ can have *at most* two real zeroes.
# 
# 
# From the coefficients of the quadratic $f$, its zeroes are:
# 
# $$
# \begin{align}
# x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}
# &&
# \mbox{and}
# &&
# x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}
# \end{align}
# $$
# 
# See in this case that we indeed have an *algebraic* (but not polynomial) function of the coefficients $(a, b, c)$ of the quadratic $f$.
# 
# ### Nature of zeroes
# 
# The polynomials coded as instances of `Poly` are all *real* polynomials. That is, their coefficients are real numbers. Similarly, instances of `Quadratic` are *real* quadratic univariates. For any real quadratic univariate, both of its zeroes will be either real or complex. This can be deduced directly from the analytic expression for the roots above:
# 
# - if the discriminant $b^2 - 4ac$ is strictly greater than zero, both roots are real;
# - if the discriminant $b^2 - 4ac$ is equal to zero, there is one real root counted with multiplicity two;
# - if the discriminant $b^2 - 4ac$ is strictly less than zero, both roots are complex.
# 
# The method `zeroes()` on any instance of `Quadratic` returns its zeroes. Based on values of its discriminant, it will return a $2$-tuple of real numbers or a $2$-tuple of complex numbers which are instances of `cplx`.
# 
# For the following quadratics:
# 
# - $-12 + 2x^2$;
# - $1 - 2x + x^2$;
# - $5 + 2x + 3x^2$
# 
# we return below their discriminant and their zeroes:

# In[6]:


qd_1 = qd.Quadratic([-12, 0, 2])
qd_2 = qd.Quadratic([1, -2, 1])
qd_3 = qd.Quadratic([5, -2, 3])

qd_list = [qd_1, qd_2, qd_3]
for q in qd_list:
    print(f"for {q}:\nits discriminant is: {q.disc}\nits zeroes are: {(str(q.zeroes()[0]), str(q.zeroes()[-1]))}\n")
                                                                       


# The value of a quadratic at a zero must be zero. And so, as a sanity check, we need to evaluate each quadratic in `qd_list` at the zeroes to make sure we indeed returned a zero. Note, since zeroes may be complex numbers, i.e., instances of `cplx`, we need to use the method `cplxEval()` from `Poly` instead of `eval()`. We see that:

# In[7]:


for q in qd_list:
    q_zros = q.zeroes()
    for zro in q_zros:
        if isinstance(zro, float):
            print(round(q.cplxEval(zro), 5))
        else:
            print(q.cplxEval(zro))
    print('\n')


# As expected each quadratic in `qd_list`, evaluated at each zero, returns zero.

# ```{note}
# 
# It was mentioned earlier that real quadratics either have two real roots or two complex roots. It is easy to construct quadratics with one complex and one real solution however. E.g., the quadratic $(x - i)(x - 1)$ has roots $x_1 = i, x_2 = 1$. Expanding out the product, $(x - i)(x - 1) = i - (i+1)x + x^2$, see that the coefficients are also a mixture of real and complex numbers. That is, this is necessarily a *complex* quadratic, not a real quadratic.
# 
# ````

# In[ ]:




