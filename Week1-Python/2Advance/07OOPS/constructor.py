'''

Constructor in Python

A constructor is a special method in Python that is automatically called when an object of a class is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.
Here is an example of a class with a constructor:

```python
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object of the Person class
person1 = Person("Alice", 30)
person1.display_info()