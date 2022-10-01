cities_visited = ''
city_visited = []

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Gets the country and times visited data for travel_log
country_visited = input('What country would you like to add?\n')
times_visited = input(f'How many times did you visit {country_visited}?\n')

#Gets the cities the user visited while in the country
while cities_visited != 'done':
    print('\nIf you no longer wish to enter a city enter [done].')
    cities_visited = input('What city did you visit?\n')
    if cities_visited != 'done':
        city_visited.append(cities_visited)
        
#Adds the additional countries and cities visited to travel_log   
travel_log.append({'country': country_visited, 'visits': times_visited, 'cities': city_visited})

print(travel_log)