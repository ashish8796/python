#slice and dice with lists

list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[1:2]
#3.4

#you want to start at the beginning, of the list you can also leave out inclusive value.
list_of_random_things[:2]
#[1, 3.4]

#to return all of the elements to the end of the list, we can leave off a final element.
list_of_random_things[1:]
#[3.4, 'a string', True]

#in OR not in concept
'this' in 'this is a string'
#True
'isa' in 'this is a string'
#False
5 not in [1, 2, 3, 4, 6]
#True
5 in [1, 2, 3, 4, 6]
#False

#mutability and order
#Mutability is about whether or not we can change an object once it has been created.
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
#['one', 2, 3, 4, 5]
#lists are mutable.

greeting = "Hello there"
greeting[0] = 'M'
#TypeError: 'str' object does not support item assignment
#strings are immutable

#Order is about whether the position of an element in the object can be used to access the element. 
#Both strings and lists are ordered.