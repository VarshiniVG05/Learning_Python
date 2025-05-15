#SUPERKEYWORDS 
# 
# 1. Class a having  display function and Constructor class b having  display function create obj for a . Create a obj for b and access a constructor by using super keywords

# class A:
#     def __init__(self):
#         print("Constructor of Class A")

#     def display(self):
#         print("Display from Class A")

# class B(A):
#     def __init__(self):
#         super().__init__()  
#         print("constructor of class B")

#     def display(self):
#         print("display from class B")

# print("object of A:")
# obj_a=A()
# obj_a.display()

# print("\nobject of B:")
# obj_b=B()
# obj_b.display()

# 2. Class c having display function have to inherit class a and class b constructor.

# class A:
#     def __init__(self):
#         print("constructor of class A")

#     def display(self):
#         print("display from class A")

# class B:
#     def __init__(self):
#         print("constructor of class B")

#     def display(self):
#         print("display from class B")

# class C(A,B):
#     def __init__(self):
#         super().__init__() 
#         B.__init__(self)    
#         print("constructor of class C")

#     def display(self):
#         print("display from class C")

# print("creating object of class C:")
# obj_c=C()
# obj_c.display()

# POLYMORPHISM

# 1.Create a function which acts as two arguments function and also three arguments function

# def add_numbers(*args):
#     if len(args)==2:
#         return args[0]+args[1]
#     elif len(args)==3:
#         return args[0]+args[1]+args[2]
#     else:
#         return "function doesn,t support."

# print(add_numbers(5,10))      
# print(add_numbers(1,2,3))     
# print(add_numbers(4)) 


# 2. create a base class called person with constructor that takes a name as a parameter .
#  Create a derived called student that inherits from  person has constructor that takes a parameter called grade. 
# Write a method in student to display name and grade of student . Use super keywords to achieve this.

# class Person:
#     def __init__(self, name):

#         self.name=name
# class Student(Person):
#     def __init__(self, name, grade):
#         super().__init__(name) 
#         self.grade=grade
#     def display_info(self):
#         print(f"Student Name:{self.name}")
#         print(f"Grade: {self.grade}")
# student1 = Student("varshini","A+")
# student1.display_info()

# 3. create a base class called vehicle with a method start that print " vehicle started" 
# create a derived class called car that inherits from vehicle and overrides the start method to print " car started”.

# class Vehicle:
#     def start(self):
#         print("vehicle started")
# class Car(Vehicle):
#     def start(self):
#         print("car started")  
# vehicle=Vehicle()
# vehicle.start() 
# car=Car()
# car.start()  

# 4. create a base class called employee with properties name and salary . 
# Create a derived class called manager that inherits from employee and adds a property department .
#  Write a method in manager to display the name , salary , and department of the manager.

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary) 
#         self.department=department
#     def display_details(self):
#         print(f"Name:{self.name}")
#         print(f"Salary:₹{self.salary}")
#         print(f"Department:{self.department}")
# manager1=Manager("varshini",120000,"finance")
# manager1.display_details()

# 5. Create a class called animal with a sound function that prints "Animal makes sounds" .create a derived class called dog that inherits from animals and overrides the sounds methods to print "dog barks " .create a another function derived class bird that inherits from animal and overrides sound method to print " birds print"

# class Animal:
#     def sound(self):
#         print("animal makes noise")
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# class Bird(Animal):
#     def sound(self):
#         print("birds chirp")
# animal=Animal()
# animal.sound()    
# d=Dog()
# d.sound()    
# b=Bird()
# b.sound()  

# ENCAPSULATION

# 1. Create a Class company with a constructor with a protected variable to access that variable. The protected variable can access child class.

# class Company:
#     def __init__(self,name):
#         self._company_name=name 
# class Employee(Company):
#     def display_company(self):
#         print(f"employee works at {self._company_name}") 
# employee= Employee("Ocean Academy")
# employee.display_company()

# 2. Create a Class company with a constructor with a private variable. With a variable name access write a method. And use.

# class Company:
#     def __init__(self, name):
#         self.__name = name

#     def access(self):
#         print("Company name is:", self.__name)
# c1 = Company("Tech Innovators")
# c1.access()

# print("Accessing private variable using name mangling:", c1._Company__name)

# ABSTRACTION 

# 1.  Create an abstract class called Bus and inherit that abstract class by a child class and use the methods.

# from abc import ABC,abstractmethod
# class Bus(ABC):
#     @abstractmethod
#     def capacity(self):
#         pass  
# class SchoolBus(Bus):
#     def capacity(self):
#         print("the school bus can carry 21 students")
# bus1=SchoolBus()
# bus1.capacity()
