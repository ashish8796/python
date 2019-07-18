#if statement
#An 'if' statement is a conditional statement that runs or skips code based on whether a condition is true or false.

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

#If, Elif, Else
#for multiple if statement
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')

#indentation
#In Python, indents conventionally come in multiples of four spaces. 
#Be strict about following this convention, because changing the indentation can completely change the meaning of the code.
#The Python Style Guide recommends using 4 spaces to indent, rather than using a tab. 
#Whichever you use, be aware that "Python 3 disallows mixing the use of tabs and spaces for indentation."

#quiz
phone_balance = 10
bank_balance = 50
##First Example - try changing the value of phone_balance
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

##Second Example - try changing the value of number
number = 147
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
concession_ticket = 1.25
adult_ticket = 2.50

if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
    message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)
