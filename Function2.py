#Given a string, return a new string made of every other character
stringBits = input()
print(stringBits[::2])

# Good Work :)

# This is in function form
def stringBits(s):
	return s[::2]

while True:
	print(stringBits(input('Enter a String: ')))

# Output
# Enter a String: Hello
# Hlo
# Enter a String: Hi  
# H
# Enter a String: Heeololeo
# Hello
