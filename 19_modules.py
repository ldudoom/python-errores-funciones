import sys # funciones para obtener informacion del sistema operativo

print(sys.path) # imprime el path de donde esta el archivo que se esta ejecutando

import re # modulo para manejo de expresiones regulares

text = 'Mi numero de telefono es 95 886 3051, el codigo de pais es 593, mi numero de la suerte es el 7'
result = re.findall('[0-9]+', text)
print(result)

import time # Manejo de horas y fechas

timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local)
print(result)

import collections # Modulo para manejo de listas

numbers = [1, 2, 3, 4, 5, 6 ,5, 4, 3, 5, 6, 7,8 , 7, 4, 3, 2]
counter = collections.Counter(numbers)
print(counter)
