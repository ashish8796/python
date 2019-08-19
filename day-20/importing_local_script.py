#Importing Local Scripts
#import - used for import Python code from other scripts
#you just type import followed by the name of the file, without the .py extension

import useful_functions

# import statement creates a module object called useful_functions, To access objects from an imported module, you need to use dot notation.

import useful_functions
useful_functions.add_five([1, 2, 3, 4])

#We can add an alias to an imported module to reference it with a different name.
import useful_functions as uf
uf.add_five([1, 2, 3, 4])

#if __name__ == "__main__" - used to avoid running executable argument in current code during importing from another file
#Or alternatively, include them in a function called main() and call this in the if main block.
