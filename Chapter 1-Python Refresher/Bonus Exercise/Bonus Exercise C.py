def calculator():
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = int(input("\nChoose operation (1-5): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"Result: {num1} x {num2} = {result}")
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero!")
    elif choice == 5:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")
    else:
        print("Invalid choice!")



continue_calc = "yes"

while continue_calc.lower() == "yes":
    calculator()
    continue_calc = input("\nWould you like to perform another calculation? (yes/no): ")

print("Thank you for using the calculator!")