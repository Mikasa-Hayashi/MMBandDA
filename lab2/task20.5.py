import numpy as np
import matplotlib.pyplot as plt

# Функция f(x) задана системой:
# - cos(cos(x)) для x <= 0
# - 1 + sqrt(x) для 0 < x
def f(x):
    result = np.zeros_like(x) # замена все на нули
    
    # x <= 0
    mask1 = x <= 0
    result[mask1] = np.cos(np.cos(x[mask1]))
    
    # 0 < x <= 4
    mask2 = x > 0
    result[mask2] = 1 + np.sqrt(x[mask2])
    
    return result


# Функция g(x) задана системой:
# - -x для x >= 1
# - -x для x < 1
# предположим g(x) = -x для всех x
def g(x):
    return -x

# f(g(x))
def f_g(x):
    return f(g(x))

# Создание массива значений на отрезке [-6, 6] (250 точек)
x = np.linspace(-6, 6, 250)

# Вычисление функций
y_f = f(x)
y_g = g(x)
y_f_g = f_g(x)

# Построение графиков
plt.figure()

# График f(x)
plt.subplot(2, 2, 1) # создание сетки 2×2 и первую ячейку
plt.plot(x, y_f, 'b-', label='f(x)') # график синей линией
plt.title('Функция f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

# График g(x)
plt.subplot(2, 2, 2) # создание сетки 2×2 и вторую ячейку
plt.plot(x, y_g, 'r-', label='g(x)') # график красной линией
plt.title('Функция g(x)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid()
plt.legend()

# График f(g(x))
plt.subplot(2, 2, 3) # создание сетки 2×2 и третью ячейку
plt.plot(x, y_f_g, 'g-', label='f(g(x))') # график зеленой линией
plt.title('Композиция f(g(x))')
plt.xlabel('x')
plt.ylabel('f(g(x))')
plt.grid()
plt.legend()

# Все графики вместе
plt.subplot(2, 2, 4) # создание сетки 2×2 и четвертую ячейку
plt.plot(x, y_f, 'b-', label='f(x)')
plt.plot(x, y_g, 'r-', label='g(x)')
plt.plot(x, y_f_g, 'g-', label='f(g(x))')
plt.title('Все функции')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.tight_layout() # автоматически регулирует расстояния между графиками
plt.show()