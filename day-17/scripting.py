#Scripting With Raw Input
#input, the built-in function, which takes in an optional string argument form user.

name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

num = int(input("Enter an integer"))#change string into integer
print("hello" * num)

result = eval(input("Enter an expression: "))#to interpret input as a python code by eval
print(result)
#If the user inputs 2 * 3, this outputs 6.