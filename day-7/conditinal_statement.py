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