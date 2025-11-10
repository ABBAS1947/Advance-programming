def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# as we see that we have been using user defined functions in the last two exercises.
# we can see the applications and uses of them

my_list = [2, 3, 4, 5]
result = calculate_product(my_list)
print(f"The list: {my_list}")
print(f"The product of all items is: {result}")