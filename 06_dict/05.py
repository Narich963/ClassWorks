# 5 zadanie
countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecador',
             'Guyana', 'Paraquay', 'Peru', 'Suriname', 'Suriname', 'Uruguay',
             'Venezuela']
set_c = set(countries)
countries = list(set_c)

countries_dict = {}
for i in range(len(countries)):
    countries_dict[f'{i + 1}'] = countries[i]
print(countries_dict)