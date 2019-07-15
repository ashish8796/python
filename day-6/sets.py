#sets
# set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
#set([1, 2, 3, 6])

#Sets support the 'in' operator
#add elements to sets using the add method
#remove elements using the pop method

fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit)  # check for element
#False

fruit.add("watermelon")  # add an element
print(fruit)
#set(['orange', 'grapefruit', 'watermelon', 'apple', 'banana'])

print(fruit.pop())  # remove a random element
#orange

print(fruit)
#set(['grapefruit', 'watermelon', 'apple', 'banana'])
