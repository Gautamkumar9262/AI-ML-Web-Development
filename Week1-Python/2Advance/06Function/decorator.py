'''
Decorator functions in Python are used to modify the behavior of other functions or methods. They are a powerful feature that allows you to wrap another function in order to extend or change its behavior without permanently modifying it. Here’s a brief overview of how decorators work and an example to illustrate their use.'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")

say_hello()