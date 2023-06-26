# Error de sintaxis
# print(1 / 0))

# Error de division por cero (0)
# print(1 / 0)

# Error de variable no declarada o no definida
# print(result)

# Error de assert
'''
suma = lambda x, y: x + (y * 2)
assert(suma(2, 2) == 4)
'''

# Excepciones propias
age = 10
if age < 18:
    raise Exception('Unicamente aceptamos mayores de edad')

print('Hola')