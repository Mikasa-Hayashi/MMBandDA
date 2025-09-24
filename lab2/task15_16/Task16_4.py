import numpy as np
import scipy.integrate as integrate

# a) Площадь под параболой y = 4 - x^2 и осью x
def f_a(x):
    return 4 - x**2

# интегрируем между точками пересечения с осью x: 4 - x^2 = 0 => x = -2..2
area_a, err_a = integrate.quad(f_a, -2, 2)

print("a) Площадь фигуры под параболой y=4-x^2:", area_a)
print("Оценка ошибки quad:", err_a)
print()

# b) Площадь под функцией y = 1/sqrt(3*x), между x=0 и x=1
# Чтобы интеграл сходился при x=0, используем небольшое смещение (или quad сам справляется)
def f_b(x):
    return 1/(np.sqrt(x)**(1/3))

area_b, err_b = integrate.quad(f_b, 0, 1)

print("b) Площадь фигуры под y=1/sqrt(3*x) от x=0 до x=1:", area_b)
print("Оценка ошибки quad:", err_b)
