print("Enter first number:")
num1 = float(input())
print("Enter second number:")
num2 = float(input())
print("Enter third number:")
num3 = float(input())

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")
