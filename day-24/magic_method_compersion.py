# #MAGIC METHOD
# #megic method for comperision
# __it__ #for < 
# __le__ #for <= 
# __eq__ #for == 
# __ne__ #for!=
# __gt__ #for >
# __ge__ #for >=

# #magic method __gt__
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + "<" + self.cont
            result += "<" + other.cont[index:]
            print(result)



spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs