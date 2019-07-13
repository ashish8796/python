#A method in Python behaves similarly to a function. Methods actually are functions that are called using dot notation.

my_string = "sebastian thrun"
print(my_string.islower())
# true

print(my_string.count('a'))
# 2

print(my_string.find('a'))
#3

#.format() method
print("Mohammed has {} balloons".format(27))
#Mohammed has 27 balloons

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
#Does your dog bite?

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
#Maria loves math and statistics

#.split() method

