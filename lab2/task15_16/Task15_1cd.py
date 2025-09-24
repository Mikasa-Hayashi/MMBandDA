import numpy as np

# функция и её производные
def f(x):
    return x**3 - 6*x + 9

approximation_roots_coords = [[-3.0, 0.0]]
approximation_extrema_coords = [[-1.42, 14.7], [1.41, 3.3]]
approximation_inflections_coords = [[0.0, 9.0]]

# корни функции (только действительные)
roots = np.roots([1, 0, -6, 9])
roots = [r.real for r in roots if np.isreal(r)]
roots_coords = np.array([[root, 0] for root in roots])

# экстремумы (решения f'(x)=0)
extrema = np.roots([3, 0, -6])  # 3x^2 - 6 = 0
extrema = [r.real for r in extrema if np.isreal(r)]
extrema_coords = np.array([[ex, f(ex)] for ex in extrema])

# точки перегиба (решения f''(x)=0)
inflections = np.roots([6, 0])  # 6x = 0
inflections = [r.real for r in inflections if np.isreal(r)]
inflections_coords = np.array([[inf, f(inf)] for inf in inflections])

# Создаем массивы разностей (delta)
delta_roots = abs(np.array(approximation_roots_coords) - roots_coords)
delta_extrema = abs(np.array(approximation_extrema_coords) - extrema_coords)
delta_inflections = abs(np.array(approximation_inflections_coords) - inflections_coords)

def format_coordinates(coords, precision=4):
    return ", ".join([f"({coord[0]:.{precision}f}; {coord[1]:.{precision}f})" for coord in coords])

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

