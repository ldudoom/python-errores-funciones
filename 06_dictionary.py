'''
Dictionary Comprehension con condicional
------------------------------------

 {key:value for var in iterable if condition}
 \_________/\__________________/\___________/
 Elemento       Ciclo donde se      Condicion
 llave-valor    extraen elementos   opcional para
                de cualquier        filtrar
                iterable            elementos
'''

import random

countries = ['Ecuador', 'Colombia', 'Bolivia', 'Peru']
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 20 }
print(result)


text = 'Hola a todos, esta es una cadena de texto de prueba'
unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)

