#Iterating Through Dictionaries with For Loops
'''
When you iterate through a dictionary using a for loop, doing it the normal way (for n in some_dict) will only give you access to the keys in the dictionary
'''
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for key in cast:
    print(key)
'''
Jason Alexander
Michael Richards
Jerry Seinfeld
Julia Louis-Dreyfus
'''
#If you wish to iterate through both keys and values, you can use the built-in method items 
for key, value in cast.items():
    print("Actor: {}        Role: {}".format(key, value))
'''
Actors: Jason Alexander     Role: George Costanza
Actors: Michael Richards     Role: Cosmo Kramer
Actors: Jerry Seinfeld     Role: Jerry Seinfeld
Actors: Julia Louis-Dreyfus     Role: Elaine Benes
'''
#items is an awesome method that returns tuples of key, value pairs, 
# which you can use to iterate over dictionaries in for loops.