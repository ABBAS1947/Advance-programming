count = 0
choice = "Y"

while choice == "Y" or choice == "y":
    count += 1
    print("Would you like to continue? (Y/N)")
    choice = input()

print(f"The loop executed {count} times.")
