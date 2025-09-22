import sympy as sp

def derivative(f, x):
    for n in range(1, 4):
        deriv = sp.diff(f, x, n)
        print(f"\nПроизводная {n}-го порядка:")
        print(deriv)

# Определяем символьную переменную
x = sp.Symbol('x', real=True, positive=True)    # real=True означает, что x - вещественное число
                                                # positive=True означает, что x > 0

# Функция a
print("Fanction a: ")
# print("=" * 60)

f_a = 3*sp.exp(-2*x) + (x**(1/3)) / sp.ln(sp.ln(x))
print("f(x) =", f_a)

# Производные
derivative(f_a, x)

# Функция b
print("\n" * 2)
print("Fanction b: ")

f_b = (7*x**4 + sp.cos(1-x)) / sp.asin(sp.asin(x))

print("f(x) =", f_b)

# Производные
derivative(f_b, x)
