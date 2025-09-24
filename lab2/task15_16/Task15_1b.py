import numpy as np
import matplotlib.pyplot as plt

# Задача 1
# Для функции f(x) = x^3 - 6x + 9
# a. Построить график в окрестности нулей;

# функция
def f(x):
    return x**3 - 6*x + 9

# корни функции (только действительные)
roots = np.roots([1, 0, -6, 9])
roots = [r.real for r in roots if np.isreal(r)]

# экстремумы (решения f'(x)=0)
extrema = np.roots([3, 0, -6])  # 3x^2 - 6 = 0
extrema = [r.real for r in extrema if np.isreal(r)]

# точки перегиба (решения f''(x)=0)
inflections = np.roots([6, 0])  # 6x = 0
inflections = [r.real for r in inflections if np.isreal(r)]

# диапазон для построения графика
all_points = roots + extrema + inflections
x_min = min(all_points) - 1
x_max = max(all_points) + 1
x = np.linspace(x_min, x_max, 500)
y = f(x)

# график
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.plot(x, y, label="f(x) = x^3 - 6x + 9")

for i, r in enumerate(roots, start=1):
    plt.scatter(r, 0, color="red", zorder=5, label="Корни функции" if i == 1 else "")
    plt.text(r, 0, f" A{i}", color="red", fontsize=10, verticalalignment="bottom")

for i, e in enumerate(extrema, start=1):
    plt.scatter(e, f(e), color="blue", zorder=5, label="Экстремумы" if i == 1 else "")
    plt.text(e, f(e), f" B{i}", color="blue", fontsize=10, verticalalignment="bottom")

for i, inf in enumerate(inflections, start=1):
    plt.scatter(inflections, f(inf), color="green", zorder=5, label="Точки перегиба" if i == 1 else "")
    plt.text(inf, f(inf), f" C{i}", color="green", fontsize=10, verticalalignment="bottom")


plt.grid(True, alpha=0.3, linestyle='--')
plt.legend()
plt.show()