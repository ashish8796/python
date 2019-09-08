#OPERATOR OVERLOADING
class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other): #method for adding two no
        n1 = self.m1 + other.m1
        n2 = self.m2 + other.m2
        s3 = Student(n1, n2)
        return s3

    def __gt__(self, other):#method for checking greater no
        v1 = self.m1 + self.m2
        v2 = other.m1 + other.m2
        if v1 > v2:
            return True
        else:
            return False

    def __str__(self):#method for printing values in string formate
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(95,53)
s2 = Student(45, 89)

s3 = s1 + s2

print("s1:",s1, "s2:",s2, "s3:",s3)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

