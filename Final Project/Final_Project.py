#Company Management System#

import time
class Manager():

    #to see how many objects such as managers and employees are defined
    counter = 0
    def __init__(self,name,age):

        self.name = name
        self.age = age
        self.language = set()
        Manager.counter += 1

    def showInfo(self):
        print(f"He/she is {self.name}, and his/her age is {self.age}")

    def addLanguage(self, new_language):

        for lang in new_language:
            self.language.add(lang)

        print("Language is adding...")
        time.sleep(1)
        return self.language

    def __len__(self):
        return len(self.language)

class Employee(Manager):

    def __init__(self,name, age, salary):
        Manager.__init__(self,name, age)
        self.salary = salary

    def getSalary(self):
        print("His/her salary is {}.".format(self.salary))

manager_1 = Manager("John",50) #"French","English","German"
manager_2 = Manager("Gloria", 45) #"English","Spanish"
manager_3 = Manager("Deniz", 35) #"Turkish", "French", "Chinese"

#Ali, Celeste and Emre are the employees of manager_1, manager_2 and manager_3 respectively
managersDict = { "Ali" : {"manager1" : manager_1}, "Celeste" : {"manager2" : manager_2}, "Emre" : {"manager3" : manager_3}}

employee_1 = Employee("Ali", 27, 1000) #"French","English","German"
employee_2 = Employee("Celeste", 22, 2000) #"English","Spanish"
employee_3 = Employee("Emre", 24, 3000) #"Turkish", "French", "Chinese"

employeesDict = { "John" : {"emp1" : employee_1}, "Gloria" : {"emp2" : employee_2}, "Deniz" : {"emp3" : employee_3}}

#put all employees' info into a list
staff = list()
staff.append(employeesDict["John"]["emp1"])
staff.append(employeesDict["Gloria"]["emp2"])
staff.append(employeesDict["Deniz"]["emp3"])

print("-----------------------------------------")
for e in staff:
    if e == staff[0]:
        print("{} can speak the following languages: {}".format(staff[0].name, e.addLanguage(["French","English","German"])))
    elif e == staff[1]:
        print("{} can speak the following languages: {}".format(staff[1].name, e.addLanguage(["English","Spanish"])))
    else:
        print("{} can speak the following languages: {}".format(staff[2].name, e.addLanguage(["Turkish", "French", "Chinese"])))

print("-----------------------------------------")
print("Total number of defined managers and employees are:",Manager.counter)
