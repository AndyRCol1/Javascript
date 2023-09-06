import utlils

keys, values = utlils.get_population()


data = [
    {
    'Country': 'Colombia',
    'Population': 300
    },
    {
    'Country': 'Bolivia',
    'Population': 200
    }
]

country = input('type country =>') 
result = utlils.popupaliton_by_country(data, country)
print(result)


