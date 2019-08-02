#Lamda expression is used for anonymous function i.e. a function without name.\
multiply = lambda x, y: x * y
print(multiply(4, 7))
#output 28

'''map() is a higher-order built-in function that takes a function and iterable as inputs,
 and returns an iterator that applies the function to each element of the iterable.
 '''
 #Quiz 
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)
#OR 
averages = list(map(lambda x: sum(x)/len(x),numbers))
print(averages)