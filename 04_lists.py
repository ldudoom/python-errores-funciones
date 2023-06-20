numbers = []
for element in range(1, 11):
    #numbers.append(element)
    numbers.append(element * 2)

print(numbers)

# [element for element in iterable]
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

numbers_v3 = [element * 2 for element in range(1, 11)]
print(numbers_v3)

'''
 [element for element in iterable if condition]
 \______/\______________________/\____________/
 Elemento    Ciclo donde se         Condicion
            extraen elementos       opcional para
           de cualquier iterable    filtrar elementos

Ejemplo:
[i*2 for i in range(1, 101) if i % 2 == 0]
'''

#numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)

print(numbers)

numbers_v2 = [i*2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)


