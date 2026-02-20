# Employee class
class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def info_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.id}")
        print(f"Employee Salary: ${self.salary}")


# Manager class (inherits Employee)
class Manager(Employee):
    def __init__(self, name, id, salary, team_size, bonus):
        super().__init__(name, id, salary)
        self.team_size = team_size
        self.bonus = bonus
        
    def approve_leave(self):
        print("Leave granted")
        
    def total_salary(self):
        total = self.salary + self.bonus
        print(f"Total Salary with Bonus: ${total}")
        
# Developer class (inherits Employee)
class Developer(Employee):
    def __init__(self, name, id, salary, programming_language, experience_year):
        super().__init__(name, id, salary)
        self.programming_language = programming_language
        self.experience_year = experience_year
    
    def code(self):
            print(f"{self.name} is coding in {self.programming_language}")
    
    

# Creating objects
emp = Employee("Siddharth", 23, 500000)
emp.info_employee()

print("\n----- Manager Details -----")

mgr = Manager("Rahul", 45, 800000, 10, 100000)
mgr.info_employee()
mgr.approve_leave()
mgr.total_salary()

print("\n----- Developer Details -----")

dev = Developer("sidd", 78, 600000, "Python", 3)
dev.info_employee()
dev.code()
