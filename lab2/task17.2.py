import numpy as np
import matplotlib.pyplot as plt

# Создание сетки значений x и y в диапазоне [-5, 5]
x = np.linspace(-5, 5, 40) # создание массива из 40 точек(3 параметр), от -100 до 100
y = np.linspace(-5, 5, 40) # создание массива из 40 точек(3 параметр), от -100 до 100
X, Y = np.meshgrid(x, y) # создание сетки координат

# Вычисление функции f(x, y) = y * e^(-x)
Z = Y * np.exp(-X)

# Создание фигуры и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # означает 1 ряд, 1 колонка, 1-й график

# Постройка поверхности (аналог persp)
surf = ax.plot_surface(X, Y, Z, cmap='viridis') # цветовая карта
                      
# Отображение осей
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

# Показ графика
plt.show()