import numpy as np
import scipy.integrate as integrate

print("=== a) ∫0^∞ cos(cos(x)) dx ===")
def f_a(x):
    return np.cos(np.cos(x))

try:
    result_a, error_a = integrate.quad(f_a, 0, np.inf, limit=1000)
    print(f"Приближенное значение: {result_a}, оценка абсолютной ошибки: {error_a}")
except Exception as e:
    print("Вычисление невозможно:", e)

print("\n=== b) ∫0^∞ x^4 * exp(-x^2) dx ===")
def f_b(x):
    return x**4 * np.exp(-x**2)

result_b, error_b = integrate.quad(f_b, 0, np.inf)
print(f"Приближенное значение: {result_b}, оценка абсолютной ошибки: {error_b}")

print("\n=== c) ∫1^∞ ln(ln(x)) / x^2 dx ===")
def f_c(x):
    return np.log(np.log(x)) / x**2

result_c, error_c = integrate.quad(f_c, 1, np.inf)
print(f"Приближенное значение: {result_c}, оценка абсолютной ошибки: {error_c}")

print("\n=== d) ∫0^π sin(sin(x)) / x dx ===")
def f_d(x):
    return np.sin(np.sin(x)) / x

# интеграл имеет особеность в x=0, используем points=[0] для интегрирования с особенностью
result_d, error_d = integrate.quad(f_d, 0, np.pi, points=[0])
print(f"Приближенное значение: {result_d}, оценка абсолютной ошибки: {error_d}")

print("\n=== e) ∫0^4 1 / (x^3 - x^2) dx ===")
# x^2*(x-1) = 0 => разрывы в x=0 и x=1
def f_e(x):
    return 1 / (x**3 - x**2)

try:
    # интегрируем с разрывом в x=0 и x=1
    result_e, error_e = integrate.quad(f_e, 0, 4, points=[0, 1])
    print(f"Приближенное значение: {result_e}, оценка абсолютной ошибки: {error_e}")
except Exception as e:
    print("Интеграл расходится или не определен:", e)
