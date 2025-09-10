class Employee:
  company =  "ASUS"
  def __init__(self,salary,name,bond,company):
   self.salary = salary #Create an instance attribute of name salary and assign it with salary :
   self.name = name
   self.bond = bond
   self.company = company
  def get_Salary(self):
    return self.salary

  def get_info(self):
    print(f"the name of the employee is {self.name}.Salary is {self.salary}.The bond is for {self.bond} years")

e1 = Employee(3400,"john",3,"Tesla")
print(e1.company)#will always print instance attribute whenever attribute present :
print(Employee.company)

##Object introspection :
print(dir(e1))

""" 
Class Attributes:
 These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.

Instance Attributes: 
These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.


"""

