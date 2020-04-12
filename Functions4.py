#Given a string, return a string where for every char in the original there are 2 characters
# doubleChar = input()
# for i in doubleChar:
#   print(i * 2, end="")

# Good job!  A cool python trick below


# We can wrap this in to List Comprehension
# Play with this and break it down and put it back to together
def doubleChar(s):	
	return ''.join([i * 2 for i in s])
		
print(doubleChar('The'))
print(doubleChar('Hi-There'))

# TThhee
# HHii--TThheerree


# What's Happening
# ''.join([i * 2 for i in s])


"""
[i * 2 for i in s]

This is the same as doing the following

# Make an Empty Array
result = []

for i in s:
	result.append(i*2)
print(result)

# By Putting the entire for loop inside '[' ']'
# python automatically appends everything to an array

# To make the formatting nicer we use join with no spaces for the delimiter
# Without the join it would like 
['TT', 'hh', 'ee']

# The whole line now looks like
''.join([i * 2 for i in s])



"""