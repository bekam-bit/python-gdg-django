from typing import List
#1
class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    
p=person("Bekam","21","Male")
print(f"Name: {p.name}\nAge: {p.age}\nGender: {p.gender}")

#2 
class Dog:
    def bark(self):
        print("woof")
d=Dog()
d.bark()

#3
class Car:
    def __init__(self,make):
        self.make=make
    def getMake(self):
        return self.make

c=Car("Rava4")
print(c.getMake())

#4
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.area=width*height

r=Rectangle(13,14)
print(r.area)

#5
class Student:
    def __init__(self,grade):
        self.__grade=grade
    def set_grade(self,grade):
        self.__grade=grade
    def get_grade(self):
        return self.__grade

s=Student("A")
print(s.get_grade())
s=Student("B")
print(s.get_grade())

#6
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def annual_salary(self):
        return self.salary * 12

e=Employee("bekam",500)
print("Name: "+e.name)
print("Monthly salary: "+str(e.salary))
print("Annual salary: "+str(e.annual_salary()))

#7
class library:
    def __init__(self,book_titles:List[str]):
        self.book_titles: List[str] = book_titles
    def add_book(self,book_title:str)->None:
        self.book_titles.append(book_title)
    def show_book(self)->List[str]:
        return self.book_titles
    
l=library(["harry potter","C++","java","python","js"])
l.add_book("pirates")
l.add_book("martin")
print(l.show_book())

#8
class Animal:
    def __init__(self,sound):
        self.sound=sound
    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    def __init__(self,sound,color):
        super().__init__(sound)
        self.color=color
    def make_sound(self):
        print(f"This cat is {self.color} and says {self.sound}")

a=Animal("meow")
a.make_sound()
c=Cat("meow","black")
c.make_sound()

#9
class vechile:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def info(self):
        print(f"The car is made in {self.year} and its brand name is {self.brand}")

class Car(vechile):
    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model
    def info(self):
        print(f"The car is made in {self.year},its brand name is {self.brand} and the model is {self.model}")

v=vechile("Toyota",2010)
v.info()
c=Car("Toyota",2010,"Corolla")
c.info()

#10
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount
    def withDraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("invalid withdrawal! balance must be greater than 0")
    def get_balance(self):
        return self.__balance

baAcc=BankAccount(0)
baAcc.deposit(1000)
print(baAcc.get_balance())
baAcc.withDraw(500)
print(baAcc.get_balance())
baAcc.withDraw(501)
print(baAcc.get_balance())
        