import numpy as np
import matplotlib.pyplot as plt

# Создаем сетку значений x и y
x = np.linspace(-100, 100, 40) # создание массива из 100 точек(3 параметр), от -100 до 100
y = np.linspace(-100, 100, 40) # создание массива из 100 точек(3 параметр), от -100 до 100
X, Y = np.meshgrid(x, y) # создание сетки координат

# Вычисляем значения функции f(x, y)
Z = X**3 - 3600*X - 50*Y**2

# Создаем фигуру и 3D-оси
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # означает 1 ряд, 1 колонка, 1-й график

# Строим поверхность
surf = ax.plot_surface(X, Y, Z, cmap='viridis')

# Настройка меток осей
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

# Показываем график
print(plt.show())