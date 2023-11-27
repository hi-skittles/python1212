import sympy as sp
from sympy import pprint

# Define the variable
x = sp.Symbol('x')

# Get the expression
expression_str = input("Enter an expression: ")

# Define the expression
expression = sp.sympify(expression_str)

# Find the derivative
derivative = expression.diff()
print("Derivative:")
pprint(derivative)

# Find the integral
integral = sp.integrate(expression)
print("Integral:")
pprint(integral)
