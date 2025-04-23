#1 A

name = input("Enter your name : ")

greeting = input("Enter the greeting you want : ")

print(f"{greeting}  {name}")

#1 B

# Area Calculator (Circle, Rectangle, Triangle)
from math import pi

shapes = {
    'circle': (lambda: pi * float(input("Enter radius: "))**2),
    'rectangle': (lambda: float(input("Enter length: ")) * float(input("Enter width: "))),
    'triangle': (lambda: 0.5 * float(input("Enter base: ")) * float(input("Enter height: ")))
}

for shape, formula in shapes.items():
    print(f"Area of {shape}: {formula():.2f}")