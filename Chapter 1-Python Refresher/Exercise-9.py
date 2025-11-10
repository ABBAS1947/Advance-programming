
int_list = [45, 12, 78, 34, 90, 23, 56, 8, 67, 41]

# in this exercise we use some basic pre defined functions like min and max, append and so on.

print("Original list:")
for num in int_list:
    print(num, end=" ")
print()


print(f"\nHighest value: {max(int_list)}")
print(f"Lowest value: {min(int_list)}")


int_list.sort()
print(f"\nAscending order: {int_list}")


int_list.sort(reverse=True)
print(f"Descending order: {int_list}")


int_list.append(99)
int_list.append(5)


print(f"\nList after appending: {int_list}")
