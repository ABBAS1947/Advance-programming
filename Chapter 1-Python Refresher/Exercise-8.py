# this is a nested for loop which loops for five times and each time it prints the number after the previous with it.
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()