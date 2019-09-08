'''
Inheritance of class - Use methods of parent class in child class.
'''

class Ashish: 
    def feature1(self):
        print("Feature 1 working")
    
    def feature2(self):
        print("Feature 2 woking")

class Praveen(Ashish): #single level inheritance
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class Jugnu:
    def feature_n(self):
        print("Featur is different")
    
class Sonam(Praveen, Jugnu): #multiple inheritance
    def feature5(self):
        print("Feature 5 working")



a1 = Ashish()
b1 = Praveen()
c1 = Sonam()

a1.feature1()
a1.feature2()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1.feature_n()
