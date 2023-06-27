import utils
import read_csv
import charts

def run():
    
    data = read_csv.read_csv('./app/data.csv')
    # country = input('Ingrese el pais a buscar: ')
    # result = utils.population_by_country(data, country.title())

    '''
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    '''
    data = list(filter(lambda item: item['Continent'] == 'South America', data))
    labels, values = utils.get_world_population(data)
    charts.generate_pie_chart(labels, values)


# Esta instruccion le dice a python que si este archivo es ejecutado desde la terminal
# ejecute la funcion run, pero si es importado como modulo desde otro archivo, entonces
# no haga nada
if __name__ == '__main__':
    run()