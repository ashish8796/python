#Lamda expression is used for anonymous function i.e. a function without name.\
multiply = lambda x, y: x * y
print(multiply(4, 7))
#output 28

#Lambda with map() built-in function
'''map() is a higher-order built-in function that takes a function and iterable as inputs,
 and returns an iterator that applies the function to each element of the iterable.
 '''
 #Quiz 
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)
#OR 
averages = list(map(lambda x: sum(x)/len(x),numbers))
print(averages)

#Lambda with Filter
"""
filter() is a higher-order built-in function that takes a function 
and iterable as inputs and returns an iterator with the elements 
from the iterable for which the function returns True. 
"""
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)
#output ['Chicago', 'Denver', 'Boston']
#OR
short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)