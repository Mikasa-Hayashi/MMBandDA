import numpy as np
import matplotlib.pyplot as plt

# Задача 2
# Для функции f(x) = 1.3x^4 - 3x^3 + 2x - 0.2x^4 + 3
# a. Построить график в окрестности локальных экстремумов

# упрощаем функцию: (1.3 - 0.2)x^4 - 3x^3 + 2x + 3 = 1.1x^4 - 3x^3 + 2x + 3
def f(x):
    return 1.1*x**4 - 3*x**3 + 2*x + 3

def f1(x):
    return 4.4*x**3 - 9*x**2 + 2

# первая производная: f'(x) = 4.4x^3 - 9x^2 + 2
extrema = np.roots([4.4, -9, 0, 2])
extrema = [r.real for r in extrema if np.isreal(r)]

# диапазон вокруг экстремумов
x_min = min(extrema) - 1
x_max = max(extrema) + 1
x = np.linspace(x_min, x_max, 600)
y = f(x)

# график
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.plot(x, y, label="f(x) = 1.1x^4 - 3x^3 + 2x + 3")

# наносим экстремумы
for i, e in enumerate(extrema, start=1):
    plt.scatter(e, f(e), color="blue", zorder=5, label="Экстремумы" if i == 1 else "")
    plt.text(e, f(e), f" B{i}", color="blue", fontsize=10, verticalalignment="bottom")

plt.grid(True, alpha=0.3, linestyle="--")
plt.legend()
plt.show()
