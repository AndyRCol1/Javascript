def get_population():
    keys = ['col','bol']
    values = [200,400]
    return keys, values

def popupaliton_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result
