text = "a,b,c,d,e"
s = text.split(",")
print(s) 
# Output: ['a', 'b', 'c', 'd', 'e']
# Splits the string at each comma and returns a list of substrings

joined_text = "-".join(s)
print(joined_text)