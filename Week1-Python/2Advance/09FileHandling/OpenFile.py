#open("file name", "mode")

# modes
# r - read
# w - write
# a - append
# r+ - read and write
# w+ - write and read
# a+ - append and read
# b - binary mode
# t - text mode
# x - create
# U - universal new line mode
# default mode is 'rt' - read text
# f = open("test.txt", "r")
# content = f.read()
# print(content)
# f.close()

file = open("C:\\Users\\gauta\\OneDrive\\Desktop\\AI-ML&Web-Jan_Goal\\Week1-Python\\2Advance\\09FileHandling\\test.txt", "r")
content = file.read()
print(content)
file.close()