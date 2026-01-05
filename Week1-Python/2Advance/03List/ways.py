#1 Using square brackets
my_list = [1,2,3,10,56, 'hello', True, 3.14]

print("Original List:", my_list)

#2 Using list constructor
my_list2 = list((4,5,6, 'world', False, 2.71))
print("List using constructor:", my_list2)

#3 Using list comprehension
my_list3 = [x for x in range(5)]   
print("List using comprehension:", my_list3)

#4 Using multiplication
my_list4 = [0] * 5
print("List using multiplication:", my_list4)

#5 Using range and list
my_list5 = list(range(1, 11))
print("List using range:", my_list5)