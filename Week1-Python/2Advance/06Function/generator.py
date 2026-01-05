#generator function in python

def generate_numbers(n):
    for i in range(n):
        yield i*i
for num in generate_numbers(5):
    print(num)