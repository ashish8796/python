#single underscore (_) helps to hide internal code from external code but in actual it does'nt hide internal code from external code. 
class Queue:
    def __init__(self, contents): #for creating instances
        self._hiddenlist = list(contents)

    def push(self, value): #for inserting value
        self._hiddenlist.insert(0, value)

    def pop(self): #for removing last element or and indexed element from mutable data structure
        return self._hiddenlist.pop(-1)

    def __repr__(self): #representation of string 
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue._hiddenlist)
queue.push(0)
print(queue._hiddenlist)
queue.pop()
print(queue._hiddenlist)
