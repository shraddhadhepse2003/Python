##class is a blueprint that defines some properties and behaviours. an object is an instance of a class that has those properties and
##behaviours attached. A class is not allocated memory whwn it it defined.
##An object is allocated memory when it is created.
##class is a logical entity whereas objects are physical entities

##a=10
##print(type(a))
##
##b='shraddha'
##print(type(b))
##
##class str
##class student
##

##class student:
##    name='shraddha'
##    email='s@gmail.com'
##    roll_no=123
##
##s=student()
##print(s.name)
##print(s.email)

##class student:
##    name='shraddha'
##    email='s@gmail.com'
##    roll_no=123
##
##    def demo(self):    #self is default parameter that represent instance of class
##        name='shraddha'
##        print(name)
##
##s=student()
###s.demo()
##
##k=student()
##k.demo
##
##
##

##class A:
##    def demo(self,department):
##        print(department)
##        print(self)
##        name='shraddha'
##        age=21
##        roll_n0=101
##        print(name,age,roll_no)
##
##    def display(self):
##        email='r@gmail.com'
##        address='thane'
##        print(email,address)
##
##a=A()
##a.demo()
##print(a)
##
##a.display()
##A.demo('K')
##a.demo('Mech')

##class student:
##    def show(self,name,roll_no):
##        print("My name is",name)
##        print("roll_no is",roll_no)
##        print("python developer")
##
##    def display(self):
##        print("java developer")
##
##s=student()
##s.show('shraddha',123)
##s.display()
##

class student:
    name='shraddha'
    email='e@'
    def show(self):
        print(self.name,self.email)
        print("python developer")
    def display(self):
        print(self.name)
        print("java developer")
a=student()
#print(a.name)
a.show()
a.display()


