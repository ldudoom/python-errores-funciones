def get_population():
    keys = ['Ecuador', 'Colombia', 'Canada', 'EE.UU.', 'Mexico', 'Bolivia', 'Argentina', 'Brasil', 'Chile']
    values = [500, 600, 1200, 1500, 900, 300, 650, 1300, 700]
    return keys, values

def population_by_country(data, country):
    return list(filter(lambda item: item['Country'] == country, data))
