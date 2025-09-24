import sympy as sp
import scipy.integrate as integrate
import numpy as np

# символическое вычисление
x = sp.symbols('x')
f = x**2 * sp.cos(sp.cos(x))

# интеграл символически (SymPy оставит unevaluated, так как нет элементарного решения)
exact_integral = sp.integrate(f, (x, 0, sp.pi/2))

# если требуется численное точное значение
exact_value = float(exact_integral.evalf())

# численное приближение через scipy
def func(x):
    return x**2 * np.cos(np.cos(x))

approx_value, error_estimate = integrate.quad(func, 0, np.pi/2)

# модуль абсолютной ошибки (оценка quad)
abs_error_estimate = error_estimate
# реальная разница между "точным" и численным значением
real_error = abs(exact_value - approx_value)

print(f"Точное значение интеграла (численно через SymPy): {exact_value}")
print(f"Приближенное значение (quad): {approx_value}")
print(f"Оценка модуля абсолютной ошибки (quad): {abs_error_estimate}")
print(f"Реальная разница: {real_error}")
