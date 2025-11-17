countries = {
    'India': 'New Delhi',
    'USA': 'Washington DC',
    'China': 'Bejing'
}

print(countries.get("India"))  # New Delhi

countries.update({'Gremany': 'Berlin'})
# {'India': 'New Delhi', 'USA': 'Washington DC', 'China': 'Bejing', 'Gremany': 'Berlin'}
print(countries)

countries.pop("India")
# {'USA': 'Washington DC', 'China': 'Bejing', 'Gremany': 'Berlin'}
print(countries)

countries.popitem()
print(countries)  # {'USA': 'Washington DC', 'China': 'Bejing'}


print(countries.items())
# dict_items([('USA', 'Washington DC'), ('China', 'Bejing')])
