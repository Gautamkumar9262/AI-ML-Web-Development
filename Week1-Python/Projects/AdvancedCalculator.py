# ================== FILE PATH ==================
dataFile = r"C:\Users\gauta\OneDrive\Desktop\AI-ML&Web-Jan_Goal\Week1-Python\Projects\History.txt"


# ================== HISTORY FUNCTIONS ==================
def show_history():
    try:
        with open(dataFile, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No History Found")
            else:
                print("\n----- Calculation History -----")
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("History file not found!")

# ================== CLEAR HISTORY FUNCTIONS ==================

def clear_history():
    open(dataFile, "w").close()
    print("History Cleared Successfully!")

# ================== SAVE HISTORY FUNCTIONS ==================


def save_history(equation, result):
    with open(dataFile, "a") as file:
        file.write(f"\n{equation} = {result}\n")


# ================== CALCULATOR ==================
def calculator():
    try:
        expr = input("Enter expression (e.g. 10 + 5): ").strip()
        v1, op, v2 = expr.split()
        print(v1)
        print(op)
        print(v2)

        v1 = float(v1)
        v2 = float(v2)

        operations = {
            '+': v1 + v2,
            '-': v1 - v2,
            '*': v1 * v2,
            '/': v1 / v2 if v2 != 0 else "Error (Divide by zero)",
            '%': v1 % v2,
            '**': v1 ** v2
        }

        if op in operations:
            result = operations[float(op)]
            print("Result:", result)
            if isinstance(result, (int, float)):
                save_history(expr, result)
        else:
            print("Invalid Operator")

    except ValueError:
        print("Invalid Input Format")
    except Exception as e:
        print("Error:", e)


# ================== PROGRAM ENTRY ==================
name = input("Enter your Full Name: ")
print(f"\n************ Welcome {name} ************")

while True:
    print("\n======= MENU =======")
    print("1. New Calculation")
    print("2. View History")
    print("3. Clear History")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        calculator()
    elif choice == '2':
        show_history()
    elif choice == '3':
        clear_history()
    elif choice == '0':
        print("Thank you for using Calculator 🤖")
        break
    else:
        print("Invalid Choice, Try Again!")
