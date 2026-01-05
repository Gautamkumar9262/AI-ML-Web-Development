list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
print("List1:", list1)
print("List2 (copy of List1):", list2)

# Modifying list2 to show that it is a separate copy
list2.append(6)
print("After modifying List2:")
print("List1:", list1)
print("List2:", list2)