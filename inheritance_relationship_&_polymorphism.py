"""
INHERITANCE
-----------

always child class inherit properties from parent class.
Properties are :- data members, member function / methods, constructor
NOTE:- we cannot inherit private data members in python
"""


###########Example -1################
"""
class Phone:
    def __init__(self,price,brand,model):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.model = model

class Features(Phone):      #Calling Parent class #inheritance syntax
    pass

p = Features(30000,"Redmi","Note 8 Pro")

print(p.brand)
"""

###########Example -2 (Inheriting Private Members)################
"""
class Phone:
    def __init__(self,price,brand,model):
        print("Inside Phone constructor")
        self.__price = price
        self.brand = brand
        self.model = model

class Features(Phone):      #Calling Parent class #inheritance syntax
    pass

p = Features(30000,"Redmi","Note 8 Pro")

print(p.__price)     #Child class cannot access Parent class hidden object(Private)

"""


###########Example -3 Polymorphism(Method Overriding)################
"""
Polymorphism=>allows us to perform the same action in many different ways.
Types:- 1. Method Overloading  2. Method Overriding  3. Operator Overloading
""
class Phone:
    def __init__(self,price,brand,model):
        print("Inside Phone constructor")
        self.__price = price
        self.brand = brand
        self.model = model

    def buy(self):
        print("Buying a Phone.")

class SmartPhone(Phone):      #Calling Parent class #inheritance syntax
    def buy(self):
        print("Buying Smartphone.")     #Method Overriding=> it will override parent class when it has same method name,arguements and return type.
        super().buy()     #Super function=> it will directly call buy()method of Parent class and after execution it will come back to same position.. Cannot acces Parent attributes

p = SmartPhone(30000,"Redmi","Note 8 Pro")

p.buy()
"""

###########Example -4 When child class have their own constructor then parent constructor will not initialize################
"""
class Parent:
    def __init__(self, num):
        print("Inside Parent class constructor")
        self.__num = num

    def get_num(self):
        return self.__num

class Child:
    def __init__(self,val, num):
        print("Inside Child class constructor")
        self.__val = val
        #self.__num = num

    def get_val(self):
        return self.__val

ch = Child(100,10)
#print("Parent Num:",ch.get_num())  #'Child' object has no attribute 'get_num' error because child attribute have their own constructor
                                   # so parent constructor will not initialized...

    
print("Child Val:",ch.get_val())
"""


###########Example -5 SUper Keyword Example(1)################
"""
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor after SUPER action")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self,price,brand,camera, os, ram):
        print("This thing print First before SUPER action")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside Constructor after SUPER action")

s = SmartPhone(5000,"Redmi",64,"Android",6)
print(s.brand)
"""

###########Example -5 SUper Keyword Example(2)################
"""
class Parent:
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val


    def get_val(self):
        return self.__val

x = Child(100,200)
print(x.get_num(), x.get_val())

"""

###########Example -5 SUper Keyword Example(3)################
"""
class Parent:
    def __init__(self):
        self.__num = 100

    def show(self):
        print("Parent",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__val = 10


    def show(self):
        print("Child",self.__val)

x = Parent()
x.show() #Parent 100
y = Child()
y.show() #Child 10

"""
################ MULTILEVEL INHERITANCE #######################
"""
class Product:
    def review(self):
        print("Product customer review...")
class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor....")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a phone")
class Smartphone(Phone):
    pass

s = Smartphone(50000,"Apple",12)
p = Phone(30000,"Blackberry",8)

s.buy()
s.review()
p.review()
"""
################ HIERARCHICAL INHERITANCE #######################
"""
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor....")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a phone")
class Smartphone(Phone):
    pass
class SmartFeatures(Phone):
    pass

s = Smartphone(50000,"Apple",12)
f = SmartFeatures(30000,"Apple",16)
s.buy()
f.buy()
"""

############ MULTIPLE INHERITANCE ################
"""
class Product:
    def buy(self):
        print("Buying a product ")

class Phone:
    def __init__(self,price, brand, camera):
        print("Inside Phone COnstructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a Phone ")

#class SMartPhone(Phone,Product):      #Method Resolution Order (MRO)
class SMartPhone(Product,Phone):       #Method Resolution Order (MRO)
    pass

s = SMartPhone(20000,"Sony",12)
s.buy()

"""

################# INHERITANCE EXMAPLE#############
"""
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        val = super().m1()+30
        return val

class C(B):
    def m1(self):
        val = self.m1()+20
        return val

obj = C()
print(obj.m1())

"""

############METHOD OVERLOADING##########
#Technically method overloading doesnt exist in python
#but we can do in different manner by putting positional arguement by default 0.
#For example
"""
class maths:
    def area(self,a,b=0):
        if b == 0:
            print("Circle area : ",3.14*a*a)
        else:
            print("Recatangle are : ",a*b)
obj = maths()
obj.area(4)
obj.area(4,5)
"""



    





























