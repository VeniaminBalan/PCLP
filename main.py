import math

def get_radius():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            return radius
        except ValueError:
            print("Invalid input. Please enter a numeric value for the radius.")

print("This program will calculate the area of a circle.")
radius = get_radius()
area = math.pi * radius ** 2
print("The area of the circle is: ", area)
