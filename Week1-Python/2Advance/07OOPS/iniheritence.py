class parent:
    def func1(self):
        print("This is function 1 from parent class")
    
    def func2(self):
        print("This is function 2 from parent class")
class child(parent):
    def func3(self):
        print("This is function 3 from child class")
    
    def func4(self):
        print("This is function 4 from child class")   
obj = child()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
# Output: