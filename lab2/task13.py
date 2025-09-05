"""
1.  Вычислить выражения с точностью в 6 значащих цифр
2.  Вычислить выражение с точностью в 3 цифры после запятой
3.  Вычислить среднее арифметическое значение длины тормозного пути для данных cars, выраженное в метрах. 
    Использовать: в 1 футе 0,3048 метра. (Ответ: 13,1м.)
"""


from math import pow, sqrt, factorial, comb, exp


def calc_exp_1():
    delimeter = factorial(7) + comb(32, 11)
    denominator = sqrt(1 / (1 + 0.2435))
    expression = pow(2, 3) + (delimeter / denominator)
    return round(expression, 6)


def calc_exp_2():
    first_part = 1 / pow(0.3532, 1/3)
    scnd_part_delimeter = 12 * exp(-1/4.8)
    scnd_part_denominator = sqrt(pow(7, -3))
    second_part = scnd_part_delimeter / scnd_part_denominator
    expression = first_part - second_part
    return round(expression, 3)