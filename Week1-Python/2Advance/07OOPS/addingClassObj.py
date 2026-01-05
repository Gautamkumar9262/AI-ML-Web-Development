class Car:
    def setDetails(self, brand, color):
        self.brand = brand
        self.color = color

    def showDetails(self):
        print(f"Car Brand: {self.brand}, Color: {self.color}")   
myCar = Car()
mycar2 = Car()
myCar.setDetails("Toyota", "Red")

mycar2.setDetails("Honda", "Blue")
myCar.showDetails() 
mycar2.showDetails()