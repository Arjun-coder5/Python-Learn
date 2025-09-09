class Employee:
  
  def __init__(self,salary,name,bond):
   self.salary = salary #Create an instance attribute of name salary and assign it with salary :
   self.name = name
   self.bond = bond

  def get_Salary(self):
    return self.salary

  def get_info(self):
    print(f"the name of the employee is {self.name}.Salary is {self.salary}.The bond is for {self.bond} years")

e1 = Employee(34000,"John Doe",4)
#print(e1.get_Saalary())

e1.get_info()