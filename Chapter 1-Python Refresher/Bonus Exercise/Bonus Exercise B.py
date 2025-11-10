locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

# Print the list and find the length
print(f"Original list: {locations}")
print(f"Length: {len(locations)}\n")

# Use sorted() to print in alphabetical order
print(f"Sorted (alphabetical): {sorted(locations)}")

# Show original list is unchanged
print(f"Original list unchanged: {locations}\n")

# Use sorted() to print in reverse alphabetical order
print(f"Sorted (reverse): {sorted(locations, reverse=True)}")

# Show original list is still unchanged
print(f"Original list still unchanged: {locations}\n")

# Use reverse() to change the order
locations.reverse()
print(f"After reverse(): {locations}\n")

# Use sort() to store in alphabetical order
locations.sort()
print(f"After sort() alphabetical: {locations}\n")

# Use sort() to store in reverse alphabetical order
locations.sort(reverse=True)
print(f"After sort() reverse: {locations}")