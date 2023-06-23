import utils

data = [
        {
            'Country': 'Ecuador',
            'Population': 500
        },
        {
            'Country': 'Colombia',
            'Population': 600
        },
        {
            'Country': 'Argentina',
            'Population': 600
        },
        {
            'Country': 'Brasil',
            'Population': 1200
        },
        {
            'Country': 'Mexico',
            'Population': 800
        },
        {
            'Country': 'Canada',
            'Population': 1200
        }
    ]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Ingrese el pais a buscar: ')
    result = utils.population_by_country(data, country.title())
    print(result)


# Esta instruccion le dice a python que si este archivo es ejecutado desde la terminal
# ejecute la funcion run, pero si es importado como modulo desde otro archivo, entonces
# no haga nada
if __name__ == '__main__':
    run()