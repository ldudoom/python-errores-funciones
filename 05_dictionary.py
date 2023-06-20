import random
'''
Dictionary Comprehension
------------------------------------

 {key:value for var in iterable}
 \_________/\__________________/
 Elemento       Ciclo donde se
 llave-valor    extraen elementos
                de cualquier 
                iterable
'''

dict = {}
for i in range(1, 6):
    dict[i] = i * 2
print(dict)

dict_v2 = {i: i * 2 for i in range(1, 6)}
print(dict_v2)

countries = ['Ecuador', 'Colombia', 'Bolivia', 'Peru']
population = {}
for country in countries:
    population[country] = random.randint(1000000, 100000000)
print(population)

population_v2 = {country: random.randint(1000000, 100000000) for country in countries}
print(population_v2)


names = ['Raul', 'Fher', 'Astrid', 'Isaac', 'Nicole']
ages = [42, 41, 2, 17, 12]
names_ages = {names[i]: ages[i] for i in range(0, len(names))}
print(names_ages)

# union de 2 listas con zip
print(list(zip(names,ages)))

names_ages_v2 = {name: age for (name, age) in zip(names, ages)}
print(names_ages_v2)

