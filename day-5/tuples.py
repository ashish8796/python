#Tuples
#It's a data type for immutable ordered sequences of elements.
#tuples are immutable

location = (13.4125, 103.866667)
print("Latitude: {}".format(location[0]))
#Latitude: 13.4125

print("Latitude:", location[0])
#('Latitude:', 13.4125)

print("Longitude: {}".format(location[1]))
#Longitude: 103.866667

print("Longitude:", location[1])
#('Longitude:', 103.866667)

#Tuples can also be used to assign multiple variables in a compact way.
dimensions = 52, 40, 100
length, width, height = dimensions    #tuple unpacking
print("The dimensions are {} x {} x {}".format(length, width, height))
#The dimensions are 52 x 40 x 100

length, width, height = 52, 40, 100 #in ome go(without using tuple unpacking)
print("The dimensions are {} x {} x {}".format(length, width, height))