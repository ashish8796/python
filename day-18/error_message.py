#Accessing Error Messages
'''When you handle an exception, you can still access its error message like this:'''
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))
#output
'''ZeroDivisionError occurred: integer division or modulo by zero'''
#If you don't have a specific error you're handling, you can still access the message like this:

try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))
#Exception is just the base class for all built-in exceptions. 