import numpy as np
import matplotlib.pyplot as plt

# Задача 1
# Для функции f(x) = x^3 - 6x + 9
# a. Построить график в окрестности нулей;

# функция
def f(x):
    return x**3 - 6*x + 9


# корни уравнения
roots = np.roots([1, 0, -6, 9])
real_roots = [r.real for r in roots if np.isreal(r)]

# диапазон вокруг действительных корней
x_min = min(real_roots) - 2
x_max = max(real_roots) + 6
x = np.linspace(x_min, x_max, 500)
y = f(x)

# график
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.plot(x, y, label="f(x) = x^3 - 6x + 9")
plt.scatter(real_roots, [0]*len(real_roots), color="red", zorder=5, label="Нули функции")
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend()
plt.show()