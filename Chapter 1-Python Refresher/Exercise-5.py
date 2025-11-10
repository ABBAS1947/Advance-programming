# this is an example of a simple while loop, if the input is y then the loop continues and if it is
# not y than the loop ends
count = 0
choice = "Y" # this is for the initial loop

while choice == "Y" or choice == "y":
    count += 1
    print("Would you like to continue? (Y/N)")
    choice = input()

print(f"The loop executed {count} times.")
