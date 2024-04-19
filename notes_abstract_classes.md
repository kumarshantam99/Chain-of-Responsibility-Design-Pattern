## What is Abstract class

An abstract class can be considered a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.

A class that contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation.

We use an abstract class while we are designing large functional units or when we want to provide a common interface for different implementations of a component. 

## Abstract Base class

By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. This capability is especially useful in situations where a third party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large code base where keeping all classes in your mind is difficult or not possible. 

By default, Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.

ABC works by decorating methods of the base class as an abstract and then registering concrete classes as implementations of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod.

Example 1:

This code defines an abstract base class called “Polygon” using the ABC (Abstract Base Class) module in Python. The “Polygon” class has an abstract method called “noofsides” that needs to be implemented by its subclasses.

There are four subclasses of “Polygon” defined: “Triangle,” “Pentagon,” “Hexagon,” and “Quadrilateral.” Each of these subclasses overrides the “noofsides” method and provides its own implementation by printing the number of sides it has.

In the driver code, instances of each subclass are created, and the “noofsides” method is called on each instance to display the number of sides specific to that shape.

 Python program showing
 abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


 Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

Output: 
I have 3 sides
I have 4 sides
I have 5 sides
I have 6 sides

Example 2: 

Here, This code defines an abstract base class called “Animal” using the ABC (Abstract Base Class) module in Python. The “Animal” class has a non-abstract method called “move” that does not have any implementation. There are four subclasses of “Animal” defined: “Human,” “Snake,” “Dog,” and “Lion.” Each of these subclasses overrides the “move” method and provides its own implementation by printing a specific movement characteristic.

 Python program showing
 abstract base class work
from abc import ABC, abstractmethod


class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

 Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()

Output:
I can walk and run
I can crawl
I can bark
I can roar

## Implementation of Abstract through Subclass
By subclassing directly from the base, we can avoid the need to register the class explicitly. In this case, the Python class management is used to recognize Plugin implementation as implementing the abstract PluginBase. 

 Python program showing
 implementation of abstract
 class through subclassing
import abc

class parent:       
    def geeks(self):
        pass

class child(parent):
    def geeks(self):
        print("child class")

 Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))

Output:
True
True

A side-effect of using direct subclassing is, it is possible to find all the implementations of your plugin by asking the base class for the list of known classes derived from it. 

## Concrete Methods in Abstract Base Classes
Concrete classes contain only concrete (normal) methods whereas abstract classes may contain both concrete methods and abstract methods.

The concrete class provides an implementation of abstract methods, the abstract base class can also provide an implementation by invoking the methods via super(). Let look over the example to invoke the method using super():  

 Python program invoking a 
 method using super()
from abc import ABC

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass ")

 Driver code
r = K()
r.rk()

Output:

Abstract Base Class
subclass 

In the above program, we can invoke the methods in abstract classes by using super(). 

## Abstract Properties in Python
Abstract classes include attributes in addition to methods, you can require the attributes in concrete classes by defining them with @abstractproperty. 

Python3
 Python program showing
 abstract properties

import abc
from abc import ABC, abstractmethod

class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
class child(parent):
     
    @property
    def geeks(self):
        return "child class"
 
 
try:
    r =parent()
    print( r.geeks)
except Exception as err:
    print (err)
 
r = child()
print (r.geeks)

Output
Can't instantiate abstract class parent with abstract methods geeks
child class

In the above example, the Base class cannot be instantiated because it has only an abstract version of the property-getter method. 

## Abstract Class Instantiation
Abstract classes are incomplete because they have methods that have nobody. If Python allows creating an object for abstract classes then using that object if anyone calls the abstract method, but there is no actual implementation to invoke.

So, we use an abstract class as a template and according to the need, we extend it and build on it before we can use it. Due to the fact, an abstract class is not a concrete class, it cannot be instantiated. When we create an object for the abstract class it raises an error. 

Python3
 Python program showing
 abstract class cannot
 be an instantiation
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

c=Animal()
Output:

Traceback (most recent call last):
  File "/home/ffe4267d930f204512b7f501bb1bc489.py", line 19, in 
    c=Animal()
TypeError: Can't instantiate abstract class Animal with abstract methods move 




## Derived classes

### Python Inheritance Syntax
The syntax of simple inheritance in Python is as follows:

poster
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}

Creating a Parent Class
A parent class is a class whose properties are inherited by the child class. Let’s create a parent class called Person which has a Display method to display the person’s information.

   
#A Python program to demonstrate inheritance
class Person(object):
   
  #Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  #To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
#Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()
Output:

Satyam 102

Creating a Child Class
A child class is a class that drives the properties from its parent class. Here Emp is another class that is going to inherit the properties of the Person class(base class).

   
class Emp(Person):
   
  def Print(self):
    print("Emp class called")
     
Emp_details = Emp("Mayank", 103)
 
#calling parent class function
Emp_details.Display()
 
#Calling child class function
Emp_details.Print()
Output:

Mayank 103
Emp class called
### Example of Inheritance in Python 
Let us see an example of simple Python inheritance in which a child class is inheriting the properties of its parent class. In this example, ‘Person’ is the parent class, and ‘Employee’ is its child class.

 
#A Python program to demonstrate inheritance
 
#Base or Super class. Note object in bracket.
#(Generally, object is made ancestor of all classes)
#In Python 3.x "class Person" is
#equivalent to "class Person(object)"
 
 
class Person(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is an employee
    def isEmployee(self):
        return False
 
 
#Inherited or Subclass (Note Person in bracket)
class Employee(Person):
 
    # Here we return true
    def isEmployee(self):
        return True
 
 
#Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
 
emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())
Output: 

Geek1 False
Geek2 True

### The super() Function
The super() function is a built-in function that returns the objects that represent the parent class. It allows to access the parent class’s methods and attributes in the child class.

Example: super() function with simple Python inheritance

In this example, we created the object ‘obj’ of the child class. When we called the constructor of the child class ‘Student’, it initialized the data members to the values passed during the object creation. Then using the super() function, we invoked the constructor of the parent class.

   
#parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
#child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age) #init function is required to access parent class properties in child class
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()
Output:

Rahul 23
Mayank 23

### Adding Properties
One of the features that inheritance provides is inheriting the properties of the parent class as well as adding new properties of our own to the child class. Let us see this with an example:

   
#parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
#child class
class Student(Person):
  def __init__(self, name, age, dob):
    self.sName = name
    self.sAge = age
    self.dob = dob
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge, self.dob)
 
obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()
Output:

Here we can see that we added a new property to the child class, i.e., date of birth (dob).

Rahul 23
Mayank 23 16-03-2000

### Multiple Inheritance

#Python example to show the working of multiple
#inheritance
 
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
 
 
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
 
 
class Derived(Base1, Base2):
    def __init__(self):
 
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.str1, self.str2)
 
 
ob = Derived()
ob.printStrs()
Output: 

Base1
Base2
Derived
Geek1 Geek2

Multilevel inheritance: When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
   
#A Python program to demonstrate inheritance
 
#Base or Super class. Note object in bracket.
#(Generally, object is made ancestor of all classes)
#In Python 3.x "class Person" is
#equivalent to "class Person(object)"
 
class Base(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
 
#Inherited or Sub class (Note Person in bracket)
class Child(Base):
 
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
#Inherited or Sub class (Note Person in bracket)
 
 
class GrandChild(Child):
 
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
 
    # To get address
    def getAddress(self):
        return self.address
 
 
#Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
Output: 

Geek1 23 Noida

### Private members of the parent class 
We don’t always want the instance variables of the parent class to be inherited by the child class i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class. 

In Python inheritance, we can make an instance variable private by adding double underscores before its name. For example:

   
#Python program to demonstrate private members
#of the parent class
 
class C(object):
    def __init__(self):
        self.c = 21
 
        # d is private instance variable
        self.__d = 42
 
 
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
 
object1 = D()
 
#produces an error as d is private instance variable
print(object1.c)
print(object1.__d)
Output : 

Here we can see that when we tried to print the variable ‘c’, its value 21 is printed on the console. Whereas when we tried to print ‘d’, it generated the error. This is because the variable ‘d’ is made private by using the underscores. It is not available to the child class ‘D’ and hence the error.

21
  File "/home/993bb61c3e76cda5bb67bd9ea05956a1.py", line 16, in 
    print (object1.d)                     
AttributeError: type object 'D' has no attribute 'd'