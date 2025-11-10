import math

def area_square():
    print("Enter the length of the square:")
    length = float(input())
    area = length ** 2
    print(f"The area of the square is: {area}")

def area_circle():
    print("Enter the radius of the circle:")
    radius = float(input())
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}")

def area_triangle():
    print("Enter the base of the triangle:")
    base = float(input())
    print("Enter the height of the triangle:")
    height = float(input())
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")

# so we just defined the function till now which process the input from the user.
# here is the where the main code is running.
print("Choose an option:")
print("1: Calculate the area of a square")
print("2: Calculate the area of a circle")
print("3: Calculate the area of a triangle")

choice = int(input())

if choice == 1:
    area_square()
elif choice == 2:
    area_circle()
elif choice == 3:
    area_triangle()
else:
    print("Invalid choice!")