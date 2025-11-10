# agian this is a loop, this time it is a for loop.
# what this does is prints "FizzBuzz" for multiples of 3 and 5, "Fizz" for multiples of 3, "Buzz" for multiples of 5, and the number otherwise, from 1 to 100.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
