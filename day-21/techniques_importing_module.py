# Techniques for Importing Modules
# There are other variants of import statements that are useful in different situations.

# To import an individual function or class from a module:
from module_name import object_name

# To import multiple individual objects from a module:
from module_name import first_object, second_object

# To rename a module:
import module_name as new_name

# To import an object from a module and rename it:
from module_name import object_name as new_name

# To import every object individually from a module (DO NOT DO THIS):
from module_name import *

# If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.
import module_name