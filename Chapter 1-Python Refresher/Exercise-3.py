print("Enter the length of side 1:")
side1 = float(input())
print("Enter the length of side 2:")
side2 = float(input())
print("Enter the length of side 3:")
side3 = float(input())

# this is a very simple way to check if the triange provided by the user is valid or not
# if the sum of 2 sides is greater than the third than it is a valid triangle.
if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side2 + side3 >= side1):
    print("This is a valid triangle!")

# to check the type of the triangles we just see how mant sides are equal and if they are even equal.
    if side1 == side2 == side3:
        print("Triangle type: Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Triangle type: Isosceles")
    else:
        print("Triangle type: Scalene")
else:
    print("This is NOT a valid triangle.")
