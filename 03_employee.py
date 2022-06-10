class Employee:
    company = "twitter"
    salary = 100


rick = Employee()
rachel =Employee()

rick.salary = 300
rachel.salary = 400

print(rick.company)
print(rachel.company)
Employee.company = "YouTube"
print(rick.company)
print(rachel.company)
print(rick.salary)
print(rachel.salary)
