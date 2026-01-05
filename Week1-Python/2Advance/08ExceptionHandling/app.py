# if 1==1:
#     print("Condition is True")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is {result}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
