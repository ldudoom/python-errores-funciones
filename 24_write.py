'''
Por defecto el metodo open() viene con permisos unicamente de lectura 'r', para poder escribir, debemos darle permisos de escritura 'w'.
A continuacion la lista de permisos que podemos usar en este metodo:

r  -> abre un archivo solo para lectura. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.

rb -> abre un archivo solo para lectura en formato binario. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado 
      de la función.

r+ -> abre un archivo para escritura y lectura. El puntero del archivo está localizado al comienzo del archivo.

w  -> abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.

wb -> abre un archivo solo para escritura en formato binario. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.

w+ -> abre un archivo para escritura y lectura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.

a  -> abre un archivo para anexo. El puntero del archivo esta al final del archivo si este existe. Es decir, el archivo está en modo anexo. Si el archivo no existe, 
      crea un nuevo archivo para escritura.
'''
with open('./23_text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nNueva linea en este archivo\n')
    file.write('Segunda linea\n')
    file.write('Otra mas\n')

