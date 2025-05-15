# 1. create a class goa and functions party,beach

# class Goa:
#     def __init__(self, name):
#         self.name=name
#         print(f"Welcome to Goa,{self.name}!")

#     def party(self):
#         print(f"{self.name} is enjoying the party in Goa")

#     def beach(self):
#         print(f"{self.name} is relaxing at the beach")

# user_name=input("enter your name:")
# trip=Goa(user_name)

# trip.party()
# trip.beach()

# 2. create class as laptop and variables and objects 

# class Laptop:
#     def __init__(self, brand, price, processor, ram):
#         self.brand=brand
#         self.price=price
#         self.processor=processor
#         self.ram=ram

#     def display_specs(self):
#         print(f"{self.brand} Laptop")
#         print(f"Price: ₹{self.price}")
#         print(f"Processor: {self.processor}")
#         print(f"RAM: {self.ram} GB")
    
# Lenovo = Laptop("Lenovo",50000,"Intel i5",8)
# HP = Laptop("HP",60000,"Intel i7",16)
# Dell = Laptop("Dell",55000,"Intel i5",8)

# Lenovo.display_specs()
# HP.display_specs()
# Dell.display_specs()

# 3. create a class called kodaikanal 

# class Kodaikanal:
#     def __init__(self, hotel_name, temperature):
#         self.tourist_name = "varshini"
#         self.location = "Kodaikanal"
#         self.hotel_name = hotel_name
#         self.temperature = temperature

#     def hotel_details(self):
#         print(f"Staying at hotel: {self.hotel_name}")
#         print(f"Total duration: {self.days_of_trip} days\n")

#     def weather_report(self):
#         print(f"The current temperature in {self.location} is {self.temperature}°C.")
#         print("Perfect weather for a peaceful vacation!\n")

# tourist=Kodaikanal()
# tourist.weather_report()
# tourist.hotel_details()

# 4. 

# class Student:
#     def __init__(self, name, roll_no, course, year, marks):
#         self.__name=name
#         self.__roll_no=roll_no
#         self.__course=course
#         self.__year=year
#         self.__marks=marks

#     def name(self):
#         return self.__name

#     def roll_no(self):
#         return self.__roll_no

#     def course(self):
#         return self.__course

#     def year(self):
#         return self.__year

#     def marks(self):
#         return self.__marks

#     def display(self):
#         print(f"Name: {self.__name}")
#         print(f"Roll No: {self.__roll_no}")
#         print(f"Course: {self.__course}")
#         print(f"Year: {self.__year}")
#         print(f"Marks: {self.__marks}%")

# student1 = Student("Varshini",67, "BCom",3,73)
# student1.display()

# INHERITANCE

# 1. Create class as dad having phone as function.Class as  son  and son has laptop function.Create a object for son and inherit a phone function from dad class
# class Dad:
#     def phone(self):
#         print("Dad's phone: Using a Samsung smartphone")

# class Son(Dad):
#     def laptop(self):
#         print("Son's laptop: Using a Dell laptop for studies")

# son1 = Son()

# son1.laptop()  
# son1.phone()

# 2. create a mom class having a sweet function inherited from dad's phone and mom's sweet.

# class Dad:
#     def phone(self):
#         print("dad is using an iPhone")

# class Mom:
#     def sweet(self):
#         print("mom made delicious sweets")

# class Daughter(Dad, Mom):
#     def laptop(self):
#         print("daughter is using a laptop for projects")

# daughter1=Daughter()

# daughter1.laptop()   
# daughter1.phone()   
# daughter1.sweet()    

# 4. Class dad class having money function son1 , class son2 , class son 3, inherit dad . - hierarchy

# class Dad:
#     def money(self):
#         print("Dad's money:₹10,00,000")

# class Son1(Dad):
#     def bike(self):
#         print("Son1's bike: splendor")

# class Son2(Dad):
#     def car(self):
#         print("Son2's car: swift")

# class Son3(Dad):
#     def laptop(self):
#         print("Son3's laptop: HP")

# print("Son1")
# s1=Son1()
# s1.money()
# s1.bike()

# print("\n Son2 ")
# s2=Son2()
# s2.money()
# s2.car()

# print("\n Son3 ")
# s3=Son3()
# s3.money()
# s3.laptop()

# 5. Class dad class having money function son1 , class son2 , class son 3, inherit dad class land having important function. Inherit dad and land inherit son1.  - hybrid

# class Dad:
#     def money(self):
#         print("Dad's money: ₹15,00,000")

# class Land:
#     def important(self):
#         print("Land property: 2 acres in hometown")

# class Son1(Dad, Land):
#     def bike(self):
#         print("Son1's bike: honda")

# class Son2(Dad):
#     def car(self):
#         print("Son2's car: ford")

# class Son3(Dad):
#     def laptop(self):
#         print("Son3's laptop: lenovo")

# print("Son1")
# s1 = Son1()
# s1.money()       
# s1.important()  
# s1.bike()  

# print("\n Son2")
# s2 = Son2()
# s2.money()   
# s2.car()        

# print("\nSon3")
# s3 = Son3()
# s3.money()    
# s3.laptop()   

# 6. Person class and a Student class that inherits from Person .

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display_person_info(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")

# class Student(Person):
#     def __init__(self,name,age,rollnumber,course):
#         super().__init__(name,age)
#         self.rollnumber=rollnumber
#         self.course = course

#     def display_student_info(self):
#         self.display_person_info()
#         print(f"Student ID: {self.rollnumber}")
#         print(f"Course: {self.course}")

# student1 = Student("varshini",20,"67","BCom")

# student1.display_student_info()

# 7. Create a class Animal, a Mammal class that inherits from Animal, and a Dog class that inherits from Mammal.

# class Animal:
#     def __init__(self, name):
#         self.name=name

#     def speak(self):
#         return f"{self.name} licks everyone."

# class Mammal(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def characteristics(self):
#         return f"{self.name} is white in colour"

# class Dog(Mammal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         return f"{self.name} barks. Woof!"

#     def info(self):
#         return f"{self.name} is a {self.breed}."

# d = Dog("Rocky","Labrador")
# print(d.speak())        
# print(d.characteristics())
# print(d.info())  

# 8. Create a class Vehicle and two classes Car and Bike that inherit from Vehicle.

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model

#     def start_engine(self):
#         return f"The engine of {self.brand} {self.model} starts."

# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)

#     def car_info(self):
#         return f"{self.brand} {self.model} is white in colour"

# class Bike(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)

#     def bike_info(self):
#         return f"{self.brand} {self.model} is black in colour"

# car = Car("honda","city")
# bike = Bike("yamaha","MT-15")

# print(car.start_engine())  
# print(car.car_info())    
# print(bike.start_engine()) 
# print(bike.bike_info())

# 9. Create a Teacher class, a Student class that both inherit from Person, and an Assistant class that inherits from both.

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def get_details(self):
#         return f"Name: {self.name}, Age: {self.age}"

# class Teacher(Person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age,subject)
#         self.subject=subject

#     def teach(self):
#         return f"{self.name} teaches {self.subject}."

# class Student(Person):
#     def __init__(self,name,age,course):
#         super().__init__(name,age)
#         self.course=course

#     def study(self):
#         return f"{self.name} studies {self.course}."

# class Assistant(Teacher,Student):
#     def __init__(self, name,age,subject,course):
#         Teacher.__init__(self,name,age,subject)
#         Student.__init__(self,name,age,course)

#     def assist(self):
#         return f"{self.name} assists in {self.subject} while studying {self.course}."

# assistant=Assistant("Sangeetha",24,"computer science","data science")

# print(assistant.get_details()) 
# print(assistant.teach())        
# print(assistant.study())     
# print(assistant.assist())  

