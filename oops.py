#example program for class and object
'''class add:
    x=8
    y=9
    def sum(self):
        print("sum:",self.x+self.y)
obj =add()
obj.sum()'''
#method2
'''class add:
    x=8
    y=9
    def sum(self):
        return self.x+self.y
obj=add()
print("sum:",obj.sum())'''
#Encapsulation
#public
'''class robo:
    x=100
    def chitti(self):
        print(self.x)
obj=robo()
obj.chitti()
print(obj.x)'''
#private
'''class robo:
    __x=100
    def __chitti(self):
        print(__self.x)

obj=robo()
obj.chitti()
print(obj.__x)'''
#abstraction
'''from abc import ABC,abstractmethod

class robo(ABC):
    @abstractmethod
    def sana(self):
        None
class chitti(robo):
    def sana(self):
        print("sum:")
obj=chitti()
obj.sana()'''
'''from abc import ABC, abstractmethod

# Define an abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclass that inherits from Shape
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

# Create an instance of Square
square = Square(5)
print("Area of the square:", square.area())'''
#constructor
#default constructor
'''class robo:
    def __init__(self):
        self.x=100
        self.y=200
obj=robo()
print("addition:",(obj.x+obj.y))'''
#parametrized constructor
'''class robo:
    def __init__(self,x,y):
        self.a=x
        self.b=y
obj=robo(100,200)
print("addition:",(obj.a+obj.b))'''
#single inheritance
'''class parent:
    def show(self):
        print("parent class")
class child(parent):
    def display(self):
        print("child class")
c=child()
c.display()
c.show()'''
#multiple inheritance
'''class father:
    def show(self):
        print("faztrher")
class mother:
    def display(self):
        print("mother")
class child(father,mother):
    def display1(self):
        print("children")
c=child()
c.show()
c.display()
c.display1()'''
#multilevel inheritance
'''class grandparent:
    def granp(self):
        print("GP")
class parent(grandparent):
    def par(self):
        print("P")        
class child(parent):
    def ch(self):
        print("CH")
c=child()
c.granp()
c.par()
c.ch()'''
#hierarchical inheritance
'''class grandparent:
    def granp(self):
        print("GP")
class parent(grandparent):
    def par(self):
        print("P")        
class child(grandparent):
    def ch(self):
        print("CH")
c=child()
p=parent()
c.granp()
p.granp()
c.ch()
p.par()'''
#hybrid inheritance
'''class base:
    def show(self):
        print("base")
class derived1(base):
    def display(self):
        print("derived1")
class derived2(base):
    def display1(self):
        print("derived2")
class derived3(derived1,derived2):
    def display2(self):
        print("derived3")
c=derived3()
c.show()
c.display()
c.display1()
c.display2()'''
#polymorphism
#dynamic or runtime polymorphism
'''def sum(*args):
    if args:
        start=type(args[0])()
        for i in args:
            start+=i
        return start
print(sum(1,2,3))
print(sum('hi','hello'))
print(sum((1,2,3),(4,5,6)))'''
#ex2
'''class A:
    def fun(self):
        print("A")
class B:
    def fun(self):
        print("B")        
class C:
    def fun(self):
        print("C")

def poly(obj):
    obj.fun()
obj1=A()
obj2=B()
obj3=C()
poly(obj1)
poly(obj2)
poly(obj3)'''
#static or compiletime(method overloading)
'''from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)
    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)
    @dispatch(str,str)
    def add(self,a,b):
        print(a+b)
obj=A()
obj.add(2,3)
obj.add(1,2,3)
obj.add('hi','   hello')'''
#method overriding
'''class derived1:
    def display(self):
        print("derived1")
class derived2(derived1):
    def display(self):
        print("derived2")
class derived3(derived2):
    def display(self):
        print("derived3")   
c=derived3()
c1=derived2()
c1.display()    
c.display()'''         
#ex2
'''class father:
    def display(self):
        print("faztrher")
class mother:
    def display(self):
        print("mother")
class child(father,mother):
        pass
c=child()
c.display()'''
#ex3
'''class derived1:
    def __init__(self):
        print("derived1")
class derived2(derived1):
    def __init__(self):
        print("derived2")
d=derived2()'''
#ex4
'''class derived1:
    def method(self):
        print("derived1")
class derived2(derived1):
    def method(self):
        derived1.method(self)
        super().method()
        print("derived2")
d=derived2()
d.method()'''
#ex5
'''class derived1:
    def __init__(self,a,b):
        self.x=a
        self.y=b
class derived2(derived1):
    def __init__(self,a,b):
        derived1.__init__(self,10,20)
obj=derived2(5,6)
print(obj.x)
print(obj.y)
print(obj.x+obj.y)'''
#ex6
'''class derived1:
    def __init__(self,a,b):
        self.x=a
        self.y=b
class derived2(derived1):
    def __init__(self,a,b):
        derived1.__init__(self,a,b)
obj=derived2(5,6)
print(obj.x)
print(obj.y)
print(obj.x+obj.y)'''
#ex7
'''class derived1:
    def __init__(self,a,b):
        self.x=a
        self.y=b
class derived2(derived1):
    def __init__(self,a,b,c,d):
        derived1.__init__(self,a,b)
        self.c=c
        self.d=d
obj=derived2(5,6,7,8)
print(obj.x)
print(obj.y)
print(obj.c)
print(obj.d)
print(obj.x+obj.y)'''
#operator overloading
'''class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        
        return A(self.x+other.x)
    def __lt__(self,other):
        if self.x < other.x:
            return True
        else:
            return False                
obj1=A(10)
obj2=A(20)
print(obj1.x+obj2.x)
print(obj1<obj2)
'''
'''class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __add__(self,other):
        if isinstance(other,A):
            return A(self.x+other.x,self.y+other.y)
            return NotImplemented
p=A(10,20)
p1=A(20,30)
print(p+p1)'''







        
        

































