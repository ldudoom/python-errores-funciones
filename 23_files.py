file = open('./23_text.txt')
# Leer el contenido completo del archivo
# print(file.read())

# Leer el archivo linea a linea, tal como un iterador
'''
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''
# Ahora vamos a leer el archivo con un buble
'''
for line in file:
    print(line)
'''

# siempre luego de un read, debemos cerrarlo para liberar memoria
file.close()

# Tenemos una instruccion de Python que nos permite abrir un archivo, y cuando se termina su procesamiento, 
# este se cierra automaticamente, liberando asi la memoria

with open('./23_text.txt') as file:
    for line in file:
        print(line)