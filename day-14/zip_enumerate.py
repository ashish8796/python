#Zip
#zip returns an iterator that combines multiple iterables into one sequence of tuples.

list(zip(['a', 'b', 'c'], [1, 2, 3])) 
#would output [('a', 1), ('b', 2), ('c', 3)].

#You could unpack each tuple in a for loop like this.
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

#you can also unzip a list into tuples using an asterisk
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters, nums)

#Enumerate
#enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

