def get_population(country_dict):
    
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    
    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values

def get_world_population(data):
    world_population_list = list(map(lambda item: {'Country/Territory': data['Country/Territory'], 'World Population Percentage': data['World Population Percentage']}, data))
    world_population_dict = {world_population_list['Country/Territory']: float(world_population_list['World Population Percentage']) for i in range(0, len(world_population_list), 2)}
    return world_population_dict.keys(), world_population_dict.values()

def population_by_country(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))
