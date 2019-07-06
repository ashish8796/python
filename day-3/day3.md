int = for integer values,

float = for decimal or floating points values
```
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0

```
Boolean Operators

Comparison Operators

```
SymbolUse Case	Bool	Operation
5 < 3	       False	Less Than
5 > 3	        True	Greater Than
3 <= 3	        True	Less Than or Equal To
3 >= 5	        False	Greater Than or Equal To
3 == 5	        False	Equal To
3 != 5	        True	Not Equal To

Logical Use	        Bool	Operation
5 < 3 and 5 == 5	False	and - Evaluates if all provided statements are True
5 < 3 or 5 == 5	    True	or - Evaluates if at least one of many statements is True
not 5 < 3	        True	not - Flips the Bool Value

```
Strings
# strings = string is the bunch of some words, numbers, etc. within double or single quotes.
```
 my_string = 'this is a string!'
 my_string2 = "this is also a string!!!"
 ```
 You can also include a \ in your string to be able to include one of these quotes:

 ```
 this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
```

Simon's skateboard is in the garage.

If we don't use this, notice we get the following error:
```
File "<ipython-input-20-e80562c2a290>", line 1
    this_string = 'Simon's skateboard is in the garage.'
                         ^
SyntaxError: invalid syntax
```
use of addition symbol
```print(first_word + second_word)```

To creat space between two words by using space between two quotes.
```print(first_word + ' ' + second_word)```

Use of multiple sign
```print(first_word * 5)```

Lenth = len() used for counting the number of character used in a string.
```print(len(first_word))```
