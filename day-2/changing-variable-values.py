# changing the variable does not change the value of the variable which was depended on that variable
#because when a variable is assigned, it is assigned to the value of the expression on the right-hand-side, not to the expression itself.

carrots = 24

rabbits = 8

crs_per_rab = carrots/rabbits

rabbits = 12
print(crs_per_rab)
#prints 3
crs_per_rab = carrots/rabbits
print(crs_per_rab)
#prints 2
