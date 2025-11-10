locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']


print(f"Original list: {locations}")
print(f"Length: {len(locations)}\n")


print(f"Sorted (alphabetical): {sorted(locations)}")


print(f"Original list unchanged: {locations}\n")


print(f"Sorted (reverse): {sorted(locations, reverse=True)}")


print(f"Original list still unchanged: {locations}\n")


locations.reverse()
print(f"After reverse(): {locations}\n")


locations.sort()
print(f"After sort() alphabetical: {locations}\n")


locations.sort(reverse=True)
print(f"After sort() reverse: {locations}")