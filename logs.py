from sympy import Symbol, S, sin, Union, Interval, oo
from sympy.calculus.util import continuous_domain

x = Symbol("x")
f = sin(x) / x
continuous_domain(f, x, S.Reals)
out = Union(Interval.open(-oo, 0), Interval.open(0, oo))
print(continuous_domain(f, x, S.Reals))
