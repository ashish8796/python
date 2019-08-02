#Functions
#Example of a function definition:
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

#After defining the cylinder_volume function, we can call the function like this.
print(cylinder_volume(10, 3)
#output 282.7431

#Default Arguments

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
print(cylinder_volume(10))

'''In the example above, radius is set to 5 
if that parameter is omitted in a function call. 
If we call cylinder_volume(10), 
the function will use 10 as the height and 5 as the radius. 
However, if we call cylinder_volume(10, 7) the 7 will simply overwrite the default value of 5.'''

# pass values in two ways - by position and by name.
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name
