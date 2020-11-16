from sympy import symbols, sqrt, simplify

a = symbols('a')

expr = (sqrt(a) - a/(sqrt(a) + 1))*((a - 1)/sqrt(a))

print(simplify(expr))