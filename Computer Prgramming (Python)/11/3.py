class Name(object):
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self,t,f,l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return (f"Full name = {self.title}{self.firstName}{self.lastName}")
    
class Date(object):
    def __init__(self,day,month,year = 0):
        self.day =day
        self.month = month
        self.year = year

    def setDate(self, d,m,y):
        self.day = d
        self.month = m
        self.year = y

    def getDate(self):
        return (self.day, self.month, self.year)
    
    def getDateBC(self):
        self.year += 543
        return (f"{self.day},{self.month}, {self.year}")

class Address():
    def __init__(self, houseno, street, district,city,country,postcode):
        self.houseno = houseno
        self.street = street
        self.district = district
        self.city = city
        self.country =country
        self.postcode = postcode
    
    def setAddress(self, houseno, street, district, city, country ,postcode):
        self.houseno = houseno
        self.street = street
        self.district = district
        self.city = city
        self.country =country
        self.postcode = postcode
        
    def getAddress(self):
        return f"{self.houseno}, {self.street}, {self.district}, {self.city}, {self.country}, {self.postcode}"
    
class Person:
    def __init__(self,name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address

    def printinfo(self):
        print(f"{self.name}\n{self.birthdate}\n{self.address}")

class Employee(Person):
    def __init__(self, name, birthdate, address,startdate, department):
        super().__init__(name, birthdate, address)
        self.startdate = startdate
        self.department = department

    def printinfo(self):
        print(f"{self.name}\n{self.birthdate}\n{self.address}\n{self.startdate}\n{self.department}")


class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startdate, department, wage):
        super().__init__(name, birthdate, address, startdate, department)
        self.wage = wage

    def printinfo(self):
        print(f"{self.name}\n{self.birthdate}\n{self.address}\n{self.startdate}\n{self.department}\n{self.wage}")


class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startdate, department, salary):
        super().__init__(name, birthdate, address, startdate, department)
        self.salary = salary

    def printinfo(self):
        print(f"{self.name}\n{self.birthdate}\n{self.address}\n{self.startdate}\n{self.department}\n{self.salary}")
    
class Department():
    def __init__(self, description, manager, employeelist):
        self.description = description
        self.manager = manager
        self.employeelist = employeelist

    def addEmployee(self, employee):
        employee.Department = self
        self.employeelist.append(employee)

    def deleteEmployee(self, employee):
        employee.Department = self
        self.employeelist.remove(employee)

    def setManager(self, employee):
        if isinstance(employee, PermEmployee) and self.employeelist.contains(employee):
            self.manager = employee

    def printinfo(self):
        print(f"{self.description}\n{self.manager}\n{self.employeelist}")

