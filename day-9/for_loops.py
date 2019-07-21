#for loops
'''
Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.
An iterable is an object that can return one of its elements at a time.
This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.
'''

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
print("Done!")

""" 
new york city
mountain view
chicago
los angeles
Done!
"""
#Using the range() Function with for Loops
#range() is a built-in function used to create an iterable sequence of numbers. 

for i in range(3):
    print("Hello!")

'''
Hello!
Hello!
Hello!
'''
range(start=0, stop, step=1)
#The range() function takes three integer arguments, the first and third of which are optional.
'''
start - first integer argument, If unspecified, 'start' defaults to 0.
stop - second integer argument, more than the last number of the sequence,must be specified.
step - third integer argumetn, the difference between each number in the sequenc, If unspecified, 'step' defaults to 1.
'''
