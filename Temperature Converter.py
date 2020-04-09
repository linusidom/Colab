Celsius = float(input())
Fahrenheit = float()
def convert(Celsius):
  Fahrenheit = ((Celsius * 9) / 5) + 32
  return Fahrenheit

print("Celsius: " + str(Celsius) + " Fahrenheit: " + str(convert(Celsius)))
