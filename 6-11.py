print('\n----6-11-----\n')
cities = {
    'beijing' : {
        'name':'beijing',
        'country':'china',
        'population':'100',
        'fact':'tiananmen'
            },
    'taiwan' : {
        'name':'taiwan',
        'country':'china',
        'population':'10',
        'fact':'baodao'
            },
    'newyork' : {
        'name':'newpork',
        'country':'America',
        'population':'30',
        'fact':'jiazhou'
            }
        }
print(cities)
for name,a in cities.items():
    print(name)
    print('它属于' + a['country'] + ',')
    print('人口有' + str(a['population']) + '人,')
    print('特色有' + a['fact'] + '.\n')
