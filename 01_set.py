'''
La manera de definir un conjunto es con las llaves, pero no tiene clave:valor, 
solo el valor, es decir unicamente los elementos del conjutno
'''
set_countries = {'Ecuador', 'Colombia', 'Peru', 'Venezuela', 'Brazil', 'Argentina', 'Chile', 'Paraguay', 'Uruguay', 'Bolivia', 'Canada'}
print(set_countries)
print(type(set_countries))

set_numbers = {22, 443, 8080, 80, 22}
print(set_numbers)
print(type(set_numbers))

set_types = {False, True, 443, 22, 'Raul', 'Fher', 33.5}
print(set_types)
print(type(set_types))

# De esta manera creamos un conjunto a partir de una cadena
set_from_string = set('Hola Mundo !!!')
print(set_from_string)
holaMundo = list(set_from_string)
print(holaMundo[3])

set_from_list = set(['Raul', 'Alejandro', 'Chauvin', 'Ojeda'])
print(set_from_list)


set_from_dictionary = set({
    'name': 'Raul',
    'lastname': 'Chauvin',
    'num_document': '1713068060',
    'birthdate': '05 Enero 1981',
    'cellphone': '0958863051'
}.values())
print(set_from_dictionary)

# No se puede generar un conjunto de una lista de diccionarios
'''
set_from_dictionary2 = set([
{
    'name': 'Raul',
    'lastname': 'Chauvin',
    'num_document': '1713068060',
    'birthdate': '05 Enero 1981',
    'cellphone': '0958863051'
},
{
    'name': 'Fher',
    'lastname': 'Morales',
    'num_document': '1002333241',
    'birthdate': '18 Abril 1981',
    'cellphone': '0987229635'
},
{
    'name': 'Astrid',
    'lastname': 'Chauvin Morales',
    'num_document': '1760317238',
    'birthdate': '07 Agosto 2020',
    'cellphone': '0984309435'
}])
print(set_from_dictionary2)
'''

# Vamos a eliminar los numeros duplicados de una lista
numbers = [1,2,3,4,5,4,3,6,7,8,6,0,2,1,0,5,4,3,9,2,10]
print(numbers)
set_from_numbers = set(numbers)
print(set_from_numbers)
unique_numbers = list(set_from_numbers).sort()
print(unique_numbers)