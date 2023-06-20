set_countries = {'Ecuador', 'Colombia', 'Peru', 'Venezuela', 'Brazil', 'Argentina', 'Chile', 'Paraguay', 'Uruguay', 'Bolivia', 'Canada'}

# longitud del conjunto
print('size: ', len(set_countries), 'elements')

# verificar si el conjunto contiene un elemento
print('Ecuador' in set_countries)

# Agregar elementos al conjunto
set_countries.add('Australia')
print(set_countries)

# Actualizar un conjunto
set_countries.update({'EE.UU.', 'Rep. Dominicana', 'Argentina'})
print(set_countries)

# remover elementos
set_countries.remove('Rep. Dominicana')
print(set_countries)

# el metodo remove devuelve un error si esque ese elemento no existe, 
# para eso odemos manejar la exception o hacer lo siguiente
set_countries.discard('Francia')
print(set_countries)

# se limpia todo el conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))
