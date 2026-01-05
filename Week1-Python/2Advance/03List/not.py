lst = [1, 2, 3, 4, 5]

check = int (input("Enter a number to check its absence in the list: "))

if check not in lst:
    print(f"{check} is not present in the list.")