#Given two strings, retuen True if either of the strings appears at the very end
# x = input()
# y = input()
# if x[-3:].lower() == y[-3:].lower():
#   print(True)
# else:
#   print(False)

# Good job!  A Few things to think about for next time
# With this question Position of the Strings doesn't matter
# The string we want could be the first or second value
# We want to check both the first and second strings against each other
# Also in our test cases, the check string could be longer than 3 characters
# We want to try and think about all kinds of test cases beyond what's shown


def end_other(s1,s2):
	if (s2.lower() in s1.lower()) or (s1.lower() in s2.lower()):
		return True
	return False

print(end_other('Hiabc', 'abc')) # True
print(end_other('AbC', 'HiaBc')) # True
print(end_other('abc', 'abXabc')) # True
print(end_other('abcdef', 'abXabcdef')) # True
print(end_other('abcdefgh', 'abXabcdef')) # False


