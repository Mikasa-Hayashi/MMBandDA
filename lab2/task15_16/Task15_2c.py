import numpy as np

def f(x):
    return 1.1*x**4 - 3*x**3 + 2*x + 3

approximation_extrema_coords = [[-0.43, 2.43], [0.554, 3.74], [1.924, 0.52]]

# первая производная: f'(x) = 4.4x^3 - 9x^2 + 2
extrema = np.roots([4.4, -9, 0, 2])
extrema = [r.real for r in extrema if np.isreal(r)]
extrema.reverse()
extrema_coords = np.array([[ex, f(ex)] for ex in extrema])

# Создаем массивы разностей (delta)
delta_extrema = abs(np.array(approximation_extrema_coords) - extrema_coords)

def format_coordinates(coords, precision=4):
    return ", ".join([f"({coord[0]:.{precision}f}; {coord[1]:.{precision}f})" for coord in coords])

print("\nЭкстремумы:")
print(format_coordinates(extrema_coords, 4))
print("Экстремумы (приближенно):")
print(format_coordinates(approximation_extrema_coords, 4))
print("Разница (расчет - приближенное):")
print(format_coordinates(delta_extrema, 4))