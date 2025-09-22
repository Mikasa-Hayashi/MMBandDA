
# Вычисляет сумму элементов на нечетных позициях
def sum_odd_positions(arr):
    result = 0
    for i in range(0, len(arr), 2): # 0, 2, 4...
        result += arr[i]
    return result

# Тестовый вектор
d = [4, -3, 6, 8, 11, 0, 5, 9, 17, 5, 3, 2, -1, 0, 4, 12]

# Вычисление суммы
result = sum_odd_positions(d)

print("d: ", d)
print("Результат: ", result)