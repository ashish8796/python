#Errors And Exceptions
""""
Syntax errors-'''occur when Python can’t interpret our code,
didn’t follow the correct syntax for Python'''
Exceptions-'''occur when unexpected things happen during execution of a program,
even if the code is syntactically correct. 
For exmaple:-
ValueError
AssertionError
IndexError
KeyError
TypeError'''
"""

#Try Statement:- use try statements to handle exceptions
#try:- only mandatory clause in a try statement,
#except:- If Python runs into an exception while running the try block,jump to the except block 
#else:- '''Python runs into no exceptions while running the try,
#it will run the code in this block after running the try block.'''
#finally:- Before Python leaves this try statement, will run the code in this finally

#Specifying Exceptions
try:
    # some code
except ValueError:
    # some code

# to address more than one type of exception, use tuple after the except with the exceptions.
try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code

#if we want to execute different blocks, can have multiple except blocks.
try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code