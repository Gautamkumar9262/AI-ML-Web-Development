try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
    
    try:
        index = int(input("Enter an index to access in a list: "))
        sample_list = [10, 20, 30, 40, 50]
        print("Element at index", index, "is", sample_list[index])
        
    except IndexError:
        print("Error: Index out of range. Please enter a valid index.")
except ValueError:
    print("Error: Invalid input! Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
    