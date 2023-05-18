travel_log = [
    {'country':'France',
    'visits':12,
    'cities':['Paris','Lille']
    },
    {'country':'Germany',
    'visits':5,
    'cities':['berlin','hamburg']
    }
]


def modify(country, times, visited_city):
    new_travel = {}
    new_travel['country'] = country
    new_travel['visits'] = times
    new_travel['cities'] = visited_city
    travel_log.append(new_travel) 

modify('Russia', 3,['Moscow', 5, ['jcz', 'wwe','csv']])
# print(travel_log)

a = {'vaib':12, 'nidhu':44}
print('a==>', a.values())

