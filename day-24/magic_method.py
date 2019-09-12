#MAGIC METHOD
#magic method for common operator 
__sub__ #for -
__mul__ #for *
__truediv__ #for /
__floordiv__ #for //
__mod__ #for %
__pow__ #for **
__and__ #for &
__xor__ #for ^
__or__ #for |

'''
The expression x + y is tranlated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then
y.__radd__(x) is called>
'''
