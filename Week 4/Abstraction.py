#1
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,H_salary):
        self.salary=H_salary
    @abstractmethod
    def calcSalary(self):
        pass

class FullTimeEmployee(Employee):
    def calcSalary(self):
        return self.salary*30

f=FullTimeEmployee(235)
print(f.calcSalary())

#2
class PartTimeEmployee(Employee):
    def calcSalary(self):
        return self.salary*30
p=PartTimeEmployee(100)
print(p.calcSalary())

#3
class Appliance(ABC):
    @abstractmethod
    def turnOn(self):
        pass
    @abstractmethod
    def turnOff(self):
        pass

class washingMachine(Appliance):
    def turnOn(self):
        return "start washing"
    def turnOff(self):
        return "stop washing"
w=washingMachine()
print(w.turnOn())
print(w.turnOff())

#4
class Teacher:
    def work(self):
        return "teach students"

class Doctor:
    def work(self):
        return "Treat patients"

professions=[Teacher(),Doctor()]
for pro in professions:
    print(pro.work())