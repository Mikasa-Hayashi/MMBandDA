"""
1.	Вычислить значения sin x  для первых ста целых чисел: 1..100.
2.	Построить график функции x  на отрезке [-2, 2]. (x  – функция, возвращающая знак числа x, т.е. +1 для положительных 
    и –1 для отрицательных, в нуле – ноль). 
3.	Объявить функцию (x) , которая возвращает два числа: целую и дробную части x. Построить их графики на отрезке [-3, 3]. 
4.	Объявить  функцию (x) =sin x x и построить ее график на отрезке[-20, 20]. Количество точек на отрезке взять равным 401. 
    Будет ли данная функция непрерывна в нуле?

"""


import numpy as np
import matplotlib.pyplot as plt
from math import sin


def calc_sin_1_to_100():
    return [sin(x) for x in range(1, 101)]


def plot_sign_function():
    x = np.linspace(-2, 2, 500)
    y = np.sign(x)
    plt.plot(x, y)
    plt.title('Sign function')
    plt.xlabel('x')
    plt.ylabel('sign(x)')
    plt.grid()
    plt.show()


def split_number(x):
    integer_part = int(x)
    fractional_part = x - integer_part
    return integer_part, fractional_part


def plot_integer_and_fractional_parts():
    x = np.linspace(-3, 3, 500)
    integer_part, fractional_part = zip(*[split_number(i) for i in x])
    plt.plot(x, integer_part, label='Integer Part')
    plt.plot(x, fractional_part, label='Fractional Part')
    plt.title('Integer and Fractional Parts')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()
    

plot_integer_and_fractional_parts()