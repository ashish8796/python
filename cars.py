# class Car:
#     runs = True

#     def __init__(self, name):
#         print("new car!")
#         self.name = name

#     def start(self):
#         if self.runs:
#             print(f"{self.name} car is started")
#         else:
#             print(f"{self.name} car is broken")



# car2 = Car()
# car1 = Car()
# my_subaru =Car("Subaru")
from collections import Counter

def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k,v in c.items() if v==m)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))