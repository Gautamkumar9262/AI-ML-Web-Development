age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

elif age == 17:
    print("You will be eligible to vote next year.")
elif age == 16:
    print("You will be eligible to vote in two years.")

elif age >=101:
    print("Please enter a valid age.")
else:
    print("You are not eligible to vote.")