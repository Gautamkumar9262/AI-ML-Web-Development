#Loop - multiple times execution of a block of code

#Types of Loops
#1. for loop
#2. while loop
#3. nested loop
#4. loop control statements (break, continue, pass)
# for loop
#syntax:
# for variable in sequence:
#     #code block   
#--------------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#--------------------------------
# while loop
#syntax:
# while condition:
#     #code block
#--------------------------------
count = 0

while count < 5:
    print("Count:", count)
    count += 1  
#--------------------------------

# nested loop
#syntax: 
# for variable1 in sequence1:
#     for variable2 in sequence2:
#         #code block
#--------------------------------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for a in adj:
    for b in fruits:
        print(a, b)
#--------------------------------
# loop control statements
# break statement
#syntax:
# for variable in sequence:
#     if condition:
#         break
#     #code block
#--------------------------------
for i in range(10):
    if i == 5:
        break
    print(i)
#--------------------------------
# continue statement
#syntax:
# for variable in sequence:
#     if condition:
#         continue
#     #code block
#--------------------------------
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#--------------------------------
# pass statement
#syntax:
# for variable in sequence:
#     if condition:
#         pass
#     #code block
#--------------------------------
for i in range(5):
    if i == 3:
        pass
    print(i)
#--------------------------------

#--------Questions---------
#1. Print all even numbers from 1 to 20 using a for loop.

for num in range(1, 21):
    if num % 2 == 0:
        print("Even:", num)
    else:
        print("Odd:", num)