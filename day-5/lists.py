#data_sturcture/lists/
#Data structures are containers that organize and group data types together in different ways.
 #A list is one of the most common and basic data structures in Python.

list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[0]
#1

list_of_random_things[len(list_of_random_things)]
```IndexError                                Traceback (most recent call last)
<ipython-input-34-f88b03e5c60e> in <module>()
----> 1 lst[len(lst)]

IndexError: list index out of range
```
list_of_random_things[len(list_of_random_things) - 1]
#True