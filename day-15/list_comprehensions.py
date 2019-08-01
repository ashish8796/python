#List Comprehensions
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title()

#can be reduced to:

capitalized_cities = [city.title() for city in cities]

#Conditionals in List Comprehensions
#only if conditional is used
squares = [x**2 for x in range(9) if x % 2 == 0]

squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
#above code will wrong answer

#if and else both conditional are used
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]