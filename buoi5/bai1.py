import random

city_names = ['Paris','London','Rome','Berlin','Marid']
city_temps ={city: random.randint(20,30) for city in city_names} #truyen so nhau nhien tu 20 den 30 vao cac bien thanh pho
print(city_temps)

above_25 = {city: temp for (city,temp) in city_temps.items() if temp > 25}
print(above_25)