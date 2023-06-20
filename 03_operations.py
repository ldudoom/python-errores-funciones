set_a = {'Colombia', 'Ecuador', 'Bolivia'}
set_b = {'Peru', 'Bolivia'}

# union de conjuntos
print('*' * 100)
print('UNION')
set_c = set_a.union(set_b)
print(set_c)
# otra manera de hacerlo
print(set_a | set_b)

# Interseccion de conjuntos
print('*' * 100)
print('INTERSECCION')
print(set_a.intersection(set_b))
# otra manera
print(set_a & set_b)

# Diferencia de conjuntos
print('*' * 100)
print('DIFERENCIA')
print(set_a.difference(set_b))
# Otra manera
print(set_a - set_b)


# Diferencia Simetrica de conjuntos
print('*' * 100)
print('DIFERENCIA SIMETRICA')
print(set_a.symmetric_difference(set_b))
# Otra manera
print(set_a ^ set_b)