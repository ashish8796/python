#Complex Boolean Expressions
#'If' statements sometimes use more complicated boolean expressions for their conditions.

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

#God and Bad examples
#Don't use True or False as conditions
if True:
    print("This indented code will always get run.")

if is_cold or not is_cold:
    print("This indented code will always get run.")

#Be careful writing expressions that use logical operators
# Bad example
if weather == "snow" or "rain":
    print("Wear boots!")

# Don't compare a boolean variable with == True or == False
#This comparison isn’t necessary, since the boolean variable itself is a boolean expression.
# Bad example
if is_cold == True:
    print("The weather is cold!")

# Good example
if is_cold:
    print("The weather is cold!")

#Truth Value Testing

# Here are most of the built-in objects that are considered False in Python:

constants defined to be false: None and False
zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
empty sequences and collections: '"", (), [], {}, set(), range(0)```

errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")