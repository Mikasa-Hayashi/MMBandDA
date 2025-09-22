b = [1, 3, 6, 8, 11, 'NA', 10, 9, 7, 5, 2, 2, 2, 0, 0]
b_cleaned = []
for x in b:
    if x != 'NA':
        b_cleaned += [x]

# поворот
b_reversed = b_cleaned[::-1]

print("Исходный вектор:")
print(b)
print("\nВектор в обратном порядке:")
print(b_reversed)