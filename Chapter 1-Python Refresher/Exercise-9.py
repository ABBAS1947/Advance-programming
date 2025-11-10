# Create an int list with 10 values
int_list = [45, 12, 78, 34, 90, 23, 56, 8, 67, 41]

# Output the list using a for loop
print("Original list:")
for num in int_list:
    print(num, end=" ")
print()

# Output the highest and lowest value
print(f"\nHighest value: {max(int_list)}")
print(f"Lowest value: {min(int_list)}")

# Sort the elements in ascending order
int_list.sort()
print(f"\nAscending order: {int_list}")

# Sort the elements in descending order
int_list.sort(reverse=True)
print(f"Descending order: {int_list}")

# Append two elements
int_list.append(99)
int_list.append(5)

# Print the list after appending
print(f"\nList after appending: {int_list}")
