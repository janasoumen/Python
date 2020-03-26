# =============================================================================

class PlayCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age =  age
    def play(self):
        print("run")
        return "done"

player1 = PlayCharacter("Soumen",37)
player2 = PlayCharacter("Arush", 5)

print(player1.name)
print(player2.age)
print(player1.play())
print(player2.play())


        

# =============================================================================
'''
# =============================================================================
class Student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student("Naveen",2)
s2 = Student("Jenny",3)

s1.show()
    
# =============================================================================
'''

'''
# =============================================================================
class Student:

    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1    # instant veriable
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3


    # Get method called Accessor
    def get_m1(self):
        return self.m1
    
    # Set method called Mutators
    def set_m1(self,value):
        self.m1 = value

    @classmethod    # Decorator
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class")


s1 = Student(34,67,32)
s2 = Student(89,32,12)

print(s1.avg())
print(Student.getSchool())
Student.info()
# =============================================================================
'''

'''
# =============================================================================
class Car:

    # Class/static varible [In memory its called Class namespace]
    wheels = 4

    def __init__(self):

        self.mil = 15        # instance veriable [In memory its called Object/instance namespace]
        self.comp = "VW"

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 6

print(c1.mil,c1.comp,c1.wheels)
print(c2.mil,c2.comp,c2.wheels)
    
# =============================================================================
'''


'''
# =============================================================================
class Computer:
    
    def __init__(self):
        self.name = "soumen"
        self.age = "35"

    def updateName(self):
        self.name = "Sujata"

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
            


if c1.compare(c2):
    print("Age of c1 and c2 are same")
else:
    print("Age of c1 and c2 are not same")


# Object c1 will take some space in Heap memory
# Who allocates size of the object? >> Constructor
# C1 is object or referring to object
# Computer() is Constructor. Call init method internally (not explicitly)
c1 = Computer()  
c2 = Computer()  
c3 = Computer()
c3.name = "Arush"
c3.age = 6

print(id(c1))
print(id(c2))

print(c1.name)
print(c2.name)
print(c3.name)
print(c3.age)
print(c1.age)
print(c2.age)

c1.updateName()

# =============================================================================
'''

'''
# First program about Class
# =============================================================================
class Computer:
    def __init__(self, cpu, ram):
        # cpu and ran just a argument now
        # object here is self.
        self.cpu = cpu
        self.ram = ram
        # print("This is init")

    def config(self):
        print("Config is: ", self.cpu, self.ram)
        # print("i5, 16gb, 1tb")


# Create a object of Computer() class
com1 = Computer("i5", 16)
com2 = Computer("i4", 32)

com1.config()
com2.config()

# Computer.config(com1)
# Computer.config(com2)
# =============================================================================
'''
