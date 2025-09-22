# Преобразование 1 в One и 2 в Two
def modify_array(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            arr[i] = 'One'
        elif arr[i] == 2:
            arr[i] = 'Two'

# Тестирование
test_array = [1, 2, 3, 1, 2, -1, -2]
print(f"До: {test_array}")
modify_array(test_array)
print(f"После: {test_array}")