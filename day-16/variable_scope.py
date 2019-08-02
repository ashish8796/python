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