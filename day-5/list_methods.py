#Useful Functions for Lists
len() #returns how many elements are in a list.
max() #returns the greatest element of the list.
#The max function is undefined for lists that contain elements from different, incomparable types.
min() #returns the smallest element in a list.
sorted() #returns a copy of a list in order from smallest to largest, leaving the list unchanged.

#.join method
#Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
#fore
#aft
#starboard
#port

name = "-".join(["García", "O'Kelly"])
print(name)
#García-O'Kelly

#append method
#A helpful method called append adds an element to the end of a list.
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
#['a', 'b', 'c', 'd', 'z']