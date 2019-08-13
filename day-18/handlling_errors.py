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

#Interesting quiz
def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")

    return(num_each, leftovers)
print(party_planner(32,3))

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")