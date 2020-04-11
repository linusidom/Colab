#Given two strings, retuen True if either of the strings appears at the very end
x = input()
y = input()
if x[-3:].lower() == y[-3:].lower():
  print(True)
else:
  print(False)
