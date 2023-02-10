
#/////////////////////////////////////////////////// inhertance
#
# class Employee:
#     counter=0
#     def __init__(self,name,salary,address):
#         self.name=name
#         self.salary=salary
#         self.address=address
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
# class Accountant(Employee):
#     def __init__(self,name,salary,address,safe):
#         super().__init__(name,salary,address)
#         self.safe=safe
#     def get_safe_name(self):
#         return  self.safe


#
# emp1=Employee(name="abdo",salary=22,address={})
# acc=Accountant(name="ahmed",salary=22,address={},safe="safe1")
# print(acc.safe)

#//////////////////////////////////////////////////////// override


class Employee:
    counter=0
    def __init__(self,name,salary,address):
        self.name=name
        self.salary=salary
        self.address=address
    def get_taxes(self):
        tax=self.salary*.2
        return self.sconver_tax_to_gpa(tax)
    @classmethod
    def increate_counter(cls):
        cls.counter+=1
    @staticmethod
    def conver_tax_to_gpa(tax):
        return tax*130

class Accountant(Employee):
    def __init__(self,name,salary,address,safe):
        super().__init__(name,salary,address)
        self.safe=safe
    def get_safe_name(self):
        return  self.safe

    def get_taxes(self):
        return self.salary * .5


emp1=Employee(name="abdo",salary=22,address={})
acc=Accountant(name="ahmed",salary=100,address={},safe="safe1")
print(acc.get_taxes())


#///////////////////////////////////////////////////// access modifer
#/////       in poython no access modifer

#///////////////////////////////////////////////////// method overload
#/////       in poython no method overload






