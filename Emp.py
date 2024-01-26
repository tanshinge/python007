# OOP WITHOUT of Getter & Setter decorators

class Employee:
    def __init__(self, first_name, last_name, emp_number):
        self.first_name = first_name 
        self.last_name = last_name
        self.emp_number = emp_number     #private

    # Getter
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    @property
    def print_emp_info(self):
        print(f"{self.emp_number}: {self.first_name} {self.last_name}")
        
        
    # Setter
    def first_name(self, var):
        self.first_name = var
        
    def last_name(self, var):
        self.last_name = var
        
    def emp_number(self, var):
        self.emp_number = var
    
    
    
    
    
    
employee001 = Employee("Jane", "Tan", "M00123")    #create an instance of Employee
# print(employee001.first_name)


employee002 = Employee("Jim", "Wong", "M00555")    #create an instance of Employee
# print(employee002._first_name)
# print(employee002.first_name, employee001.last_name, employee001.emp_number)


employee003 = Employee("Choi", "YJ", "M00333")    #create an instance of Employee
# print(employee003.first_name, employee003.last_name, employee003.emp_number)


employee002.first_name="Jim Joseph" #makes use of setter
# print(employee002.first_name)


# print(employee001.full_name)
# employee002.print_emp_info