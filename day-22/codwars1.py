class Student:


    def __init__(self, name, rollno):
        self.name = name 
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        return (self.name, self.rollno)

    class Laptop:


        def __init__(self):
            self.brand = "HP" 
            self.cpu = "i5"
            self.ram = 8  
    
p = Student("Ashish", "17ME72")
q = Student("Aman", "17ME79")

# print(p.show())
# print(q.show())
print(p.name, p.rollno, p.lap.brand)
print(q.name, q.rollno)