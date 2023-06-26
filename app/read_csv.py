# Importamos el paquete para poder procesdar archivos CSV
import csv

# Vamos a crear una funcion que haga el procesamiento del archivo
def read_csv(path):
    # Abrimos el archivo fila por file para leerlo y procesarlo
    with open(path, 'r') as csvfile:
        # Vamos a utilizar un metodo del paquete csv para obtener la informacion del archivo
        reader = csv.reader(csvfile, delimiter = ',')
        # Vamos a obtener el nombre de las columnas de esta manera, ya que sabemos que la primera fila son las cabeceras del archivo
        header = next(reader)
        # vamos a generar una variable de tipo lista para devolver los registros de la lectura de este archivo
        data = []
        # Recorremos las filas del archivo con un bucle for
        for row in reader:
            # Por ahora, solo vamos a imprimir cada una de las filas para ver el resultado
            '''
            print('*' * 200)
            print(row)
            '''
            # Ahora vamos a usar un zip para unir el header con cada una de las filas
            iterable = zip(header, row)
            # Ahora vamos a generar un diccionario de estas tuplas, utilizando el concepto de Dictionary Comprehension
            country_dictionary = {key: value for key, value in iterable}
            # Agregamos cada uno de estos diccionarios generados a la lista que declaramos previamente
            data.append(country_dictionary)
        
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data)