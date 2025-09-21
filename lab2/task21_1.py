import numpy as np
import matplotlib.pyplot as plt

# Отрезок [0, 13]
x0 = 0
x1 = 13

h = 0.1 # Шаг 
y0 = 1 # Начальное значение

x_values = np.arange(x0, x1 + h, h)

# Рассчётные значения
y_values = np.zeros(len(x_values))
y_values[0] = y0

# Решение по формуле Эйлера: y|k+1 = y|k + h * f(x|k, y|k)
for i in range(1, len(x_values)):
    y_values[i] = y_values[i-1] + h * (-np.sin(np.sin(x_values[i-1])))


# Ожидаемые значения
y_values_exact = np.zeros(len(x_values))
y_values_exact[0] = y0

# Точное решение: y(x) = cos(cos(x))
for i in range(len(x_values)):
    y_values_exact[i] = np.cos(np.cos(x_values[i]))

# Построим график для сравнения
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, 'red', linewidth=2, label='Метод Эйлера (y\' = -sin(sin(x)))')
plt.plot(x_values, y_values_exact, 'blue', linewidth=2, label='Точное решение (y = cos(cos(x)))')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Сравнение решения задачи Коши методом Эйлера с точным решением')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()