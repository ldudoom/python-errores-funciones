numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

# Ahora lo mismo usando map
numbers_v3 = list(map(lambda x: x * 2, numbers))
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2)) # devolvera una lista de longiud 3 debido a que es el tamaño de la lista mas pequeña

print(numbers_1)
print(numbers_2)
print(result)