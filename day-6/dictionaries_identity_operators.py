#Dictionaries
#A dictionary is a mutable data type that stores mappings of unique keys to values.

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
#2

elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print(elements)
#{'helium': 2, 'lithium': 3, 'hydrogen': 1, 'carbon': 6}

#dictionaries also alows 'in' operator like list.
print("carbon" in elements)
#True

#.get()
#get looks up values in a dictionary, but unlike square brackets, get returns None (or a default value of your choice) if the key isn't found.
print(elements.get("dilithium"))
#None

#Identity Operators
#Keyword	                        Operator
is	                               # evaluates if both sides have the same identity
is not	                           # evaluates if both sides have different identities
n = elements.get("dilithium")
print(n is None)
#True
print(n is not None)
#False

#question
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

print(population.get('Happy', 'There\'s no such thing.'))
#There's  no such thing.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c) #False why?
#True,True,True,False