#Variable Scope
'''If a variable is created inside a function,
 it can only be used within that function. Accessing it outside that function is not possible. '''
 # This will result in an error

def some_function():
    word = "hello"

print(word)
#word is said to have scope that is only local to each function.
#This means you can use the same name for different variables that are used in different functions.
# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"
#Here, word is said to have a global scope.
# This works fine
word = "hello"

def some_function():
    print(word)

some_function()
'''
the value of a global variable can not be modified inside the function. 
If you want to modify that variable's value inside this function, 
it should be passed in as an argument.
'''
#A better way to write this would be:

egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)