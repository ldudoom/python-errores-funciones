# para usar reduce debemos importar esta libreria
import functools

numbers = [1, 2, 3, 4]
suma = functools.reduce(lambda accumulator, item: accumulator + item, numbers)

print(numbers)
print(suma)