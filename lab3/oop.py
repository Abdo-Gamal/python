

# class Employee:
#     def __init__(self,name,age,salary,address):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.address=address
#
#
# emp1=Employee("abdo",22,23,{"city":"assuit"})
# print(emp1.address)

# /////////////////////////////////// ///////////////////////////  static varible


# class Employee:
#     static_var=True
#     def __init__(self,name,age,salary,address):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.address=address
#
#
# emp1=Employee("abdo",22,23,{"city":"assuit"})
# emp2=Employee("ahmed",22,43,{"city":"assuit"})
# print(emp1.static_var)
# print(emp2.static_var)


# /////////////////////////////////// ///////////////////////////   instance method

# class Employee:
#
#     def __init__(self,name,age,salary,address):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.address=address
#     def get_taxes(self):
#         return self.salary*.2
#
# emp1=Employee("abdo",22,50,{"city":"assuit"})
# emp2=Employee("ahmed",22,100,{"city":"assuit"})
#
# print(emp1.get_taxes())
# print(emp2.get_taxes())

 # /////////////////////////////////// /////////////////////////// class method

# class Employee:
#     counter=0
#     def __init__(self,name,age,salary,address):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.address=address
#     def get_taxes(self):
#         return self.salary*.2
#     @classmethod
#     def increate_counter(cls):
#         cls.counter+=1
#
#
#
#
# emp1=Employee("abdo",22,50,{"city":"assuit"})
# emp2=Employee("ahmed",22,100,{"city":"assuit"})
# Employee.increate_counter()
# emp1.increate_counter()
# print(Employee.counter)

# //////////////////////////////////////////////////////////////// static method


# class Employee:
#     counter=0
#     def __init__(self,name,age,salary,address):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.address=address
#
#     def get_taxes(self):
#         tax=self.salary*.2
#         return self.sconver_tax_to_gpa(tax)
#     @classmethod
#     def increate_counter(cls):
#         cls.counter+=1
#     @staticmethod
#     def conver_tax_to_gpa(tax):
#         return tax*130
#
#
# emp1=Employee("abdo",22,50,{"city":"assuit"})
# emp2=Employee("ahmed",22,100,{"city":"assuit"})
#
