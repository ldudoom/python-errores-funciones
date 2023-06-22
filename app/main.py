import utils

keys, values = utils.get_population()
print(keys, values)

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

country = input('Ingrese el pais a buscar: ')
result = utils.population_by_country(data, country.title())
print(result)