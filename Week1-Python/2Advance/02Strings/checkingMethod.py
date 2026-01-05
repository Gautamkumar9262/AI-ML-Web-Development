str = "Python"
print(str.startswith("Py"))  # Output: True
print(str.endswith("on"))    # Output: True

############False Cases##############
print(str.startswith("thon"))  # Output: False
print(str.endswith("Py"))      # Output: False  

print(str.isalpha())  # Output: True
print(str.isdigit())  # Output: False
print(str.isalnum())  # Output: True