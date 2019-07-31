#Method 1: Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
#Step 1: Create an empty dictionary.
word_counter = {}
'''
Step 2. Iterate through each element in the list. 
If an element is already included in the dictionary, add 1 to its value. 
If not, add the element to the dictionary and set its value to 1.
'''
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
#{'holmes': 1, 'great': 2, 'huckleberry': 1, 'of': 2, 'expectations': 1, 'adventures': 2, 'gasby': 1, 'sherlock': 1, 'the': 2, 'hamlet': 1, 'fin': 1}

#Method 2: Using the get method
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

#Step 1: Create an empty dictionary
word_counter = {}

#Step 2. Iterate through each element, get() its value in the dictionary, and add 1.
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1