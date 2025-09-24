import numpy as np
import matplotlib.pyplot as plt

# Задача 3
# Для функции f(x) = x^4 - 2x^3 - 8x^2 + 18x - 9
# На отрезке [-3.5; 3.5] приближенно найти корни, локальные экстремумы и точки перегиба

def f(x):
    return x**4 - 2*x**3 - 8*x**2 + 18*x - 9

def format_coordinates(coords, precision=4):
    return ", ".join([f"({coord[0]:.{precision}f}; {coord[1]:.{precision}f})" for coord in coords])

# корни функции (только действительные, в пределах [-3.5;3.5])
roots = np.roots([1, -2, -8, 18, -9])
roots = [r.real for r in roots if np.isreal(r) and -3.5 <= r.real <= 3.5]
roots_coords = np.array([[root, 0] for root in roots])

# экстремумы (решения f'(x)=0, только действительные, в пределах [-3.5;3.5])
extrema = np.roots([4, -6, -16, 18])
extrema = [r.real for r in extrema if np.isreal(r) and -3.5 <= r.real <= 3.5]
extrema_coords = np.array([[ex, f(ex)] for ex in extrema])

# точки перегиба (решения f''(x)=0, только действительные, в пределах [-3.5;3.5])
inflections = np.roots([12, -12, -16])
inflections = [r.real for r in inflections if np.isreal(r) and -3.5 <= r.real <= 3.5]
inflections.reverse()
inflections_coords = np.array([[inf, f(inf)] for inf in inflections])

# диапазон для построения графика
x = np.linspace(-3.5, 3.5, 600)
y = f(x)

# график
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)
plt.plot(x, y, label="f(x) = x^4 - 2x^3 - 8x^2 + 18x - 9")

# корни
for i, r in enumerate(roots, start=1):
    plt.scatter(r, 0, color="red", zorder=5, label="Корни функции" if i == 1 else "")
    plt.text(r, 0, f" A{i}", color="red", fontsize=10, verticalalignment="bottom")

# экстремумы
for i, e in enumerate(extrema, start=1):
    plt.scatter(e, f(e), color="blue", zorder=5, label="Экстремумы" if i == 1 else "")
    plt.text(e, f(e), f" B{i}", color="blue", fontsize=10, verticalalignment="bottom")

# точки перегиба
for i, inf in enumerate(inflections, start=1):
    plt.scatter(inf, f(inf), color="green", zorder=5, label="Точки перегиба" if i == 1 else "")
    plt.text(inf, f(inf), f" C{i}", color="green", fontsize=10, verticalalignment="bottom")

plt.grid(True, alpha=0.3, linestyle="--")
plt.legend()
plt.show()

approximation_roots_coords = [[-3.0, 0.0], [3.0, 0.0]]
approximation_extrema_coords = [[-1.88, -45.2], [2.39, -6.5], [1.0, 0.0]]
approximation_inflections_coords = [[-0.76, -26.3], [1.75, -3.5]]

# Создаем массивы разностей (delta)
delta_roots = abs(np.array(approximation_roots_coords) - roots_coords)
delta_extrema = abs(np.array(approximation_extrema_coords) - extrema_coords)
delta_inflections = abs(np.array(approximation_inflections_coords) - inflections_coords)

print("Корни функции (нули):")
print(format_coordinates(roots_coords, 4))
print("Корни функции (нули приближенно):")
print(format_coordinates(approximation_roots_coords, 4))
print("Разница (расчет - приближенное):")
print(format_coordinates(delta_roots, 4))

print("\nЭкстремумы:")
print(format_coordinates(extrema_coords, 4))
print("Экстремумы (приближенно):")
print(format_coordinates(approximation_extrema_coords, 4))
print("Разница (расчет - приближенное):")
print(format_coordinates(delta_extrema, 4))

print("\nТочки перегиба:")
print(format_coordinates(inflections_coords, 4))
print("Точки перегиба (приближенно):")
print(format_coordinates(approximation_inflections_coords, 4))
print("Разница (расчет - приближенное):")
print(format_coordinates(delta_inflections, 4))