class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

eric = Employee()
eric.salary = 100000
eric.getSalary() # Employee.getSalary(harry)