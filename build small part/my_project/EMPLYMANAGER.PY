class Employee:
    # CLASS VARIABLE
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # INSTANCE VARIABLES
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp3 = Employee("Charlie", 55000)

# All share the same company
print(emp1.company)  # TechCorp
print(emp2.company)  # TechCorp
print(emp3.company)  # TechCorp

# Different salaries (instance variables)
print(emp1.salary)  # 50000
print(emp2.salary)  # 60000

# Check employee count (class variable)
print(Employee.employee_count)  # 3

# Change class variable - affects ALL instances
Employee.company = "NewTech Inc"
print(emp1.company)  # NewTech Inc
print(emp2.company)  # NewTech Inc
print(emp3.company)  # NewTech Inc