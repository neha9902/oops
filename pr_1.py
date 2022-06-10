class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")


shreya = Programmer("Shreya", "Skype")
alka = Programmer("Alka", "GitHub")
shreya.getInfo()
alka.getInfo()