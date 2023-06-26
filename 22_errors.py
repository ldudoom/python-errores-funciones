'''
try:
    print(1 / 0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno es igual a uno' 
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('Unicamente aceptamos mayores de edad')
except Exception as error:
    print(error)
'''


# Vamos a hacerlo todo de una sola vez
try:
    print(1 / 0)
    assert 1 != 1, 'Uno es igual a uno' 
    age = 10
    if age < 18:
        raise Exception('Unicamente aceptamos mayores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)


print('Hola')