"""
1.  Вычислить выражения с точностью в 6 значащих цифр
2.  Вычислить выражение с точностью в 3 цифры после запятой
3.  Вычислить среднее арифметическое значение длины тормозного пути для данных cars, выраженное в метрах. 
    Использовать: в 1 футе 0,3048 метра. (Ответ: 13,1м.)
"""


from math import pow, sqrt, factorial, comb


def calc_exp_1():
    delimeter = factorial(7) + comb(32, 11)
    denominator = sqrt(1 / (1 + 0.2435))
    expression = pow(2, 3) + (delimeter / denominator)
    return round(expression, 6)

