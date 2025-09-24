import numpy as np
from scipy.integrate import quad

# Точное значение
def exact_integral():
    cube_root_2 = 2**(1/3)
    return 3/4 * (1 - 2 * cube_root_2)

# Подынтегральная функция
def f(x):
    return np.cbrt(x - 2)

# Приближённое вычисление методом quad
def approximate_integral():
    result, error_estimate = quad(f, 0, 1)
    return result, error_estimate

# Вычисления
exact_val = exact_integral()
approx_val, estimated_error = approximate_integral()
actual_error = abs(exact_val - approx_val)

print(f"Точное значение: {exact_val:.10f}")
print(f"Приближённое значение: {approx_val:.10f}")
print(f"Оценка погрешности quad: {estimated_error:.2e}")
print(f"Реальная погрешность: {actual_error:.2e}")
print(f"Разница: {abs(estimated_error - actual_error):.2e}")