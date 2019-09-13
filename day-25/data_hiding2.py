#Strongly private methods using double underscore (__)

class Spam:
    __egg = 6
    
    def print_egg(self):
        print(self.__egg)


s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg) #produes an error of AttributeError
