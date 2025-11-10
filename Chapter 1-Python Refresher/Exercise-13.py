def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Main program
my_list = [2, 3, 4, 5]
result = calculate_product(my_list)
print(f"The list: {my_list}")
print(f"The product of all items is: {result}")