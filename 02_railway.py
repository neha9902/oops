class RailwayForm:
    formtype = "Railway Form"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

neha = RailwayForm()
neha.name = "neha"     
neha.train = "Rajdhani Express"  
neha.printData() 