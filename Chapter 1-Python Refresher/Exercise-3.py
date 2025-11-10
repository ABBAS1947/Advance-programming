print("Enter the length of side 1:")
side1 = float(input())
print("Enter the length of side 2:")
side2 = float(input())
print("Enter the length of side 3:")
side3 = float(input())

# Check triangle inequality
if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side2 + side3 >= side1):
    print("This is a valid triangle!")

    # Extension: Classify triangle type
    if side1 == side2 == side3:
        print("Triangle type: Equilateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Triangle type: Isosceles")
    else:
        print("Triangle type: Scalene")
else:
    print("This is NOT a valid triangle.")
