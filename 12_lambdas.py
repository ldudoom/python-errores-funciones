def increment(x):
    return x + 1

result = increment(10)
print(result)

# Vamos a transformar la logica de arriba en una funcion lambda

increment_v2 = lambda x: x + 1
result_v2 = increment_v2(10)
print(result_v2)

# Ejemplo con una lista
mi_lista = [1, 2, 3, 4, 5, 6]
lista_nueva = list(map(lambda x: x * 2, mi_lista))
print(lista_nueva)  # [2, 4, 6, 8, 10, 12]


# Otro ejemplo
full_name = lambda name, lastname: f'Nombre completo es {name.title()} {lastname.title()}'
text = full_name('raul', 'chauvin')
print(text)