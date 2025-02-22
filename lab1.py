import math
'''celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")'''


a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

if a + b > c and a + c > b and b + c > a:
    print("The area of the triangle is ",area,"square units.")
else:
    print("The given sides do not form a valid triangle.")

