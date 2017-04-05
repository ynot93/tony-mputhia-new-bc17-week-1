def fizz_buzz(x):
    # Returns 'FizzBuzz' if the argument is divisible by both 3 and 5
    if x % 15 == 0:
        print("FizzBuzz")
    # Returns 'Fizz' if the argument is divisible by both 3 and 5
    elif x % 3 == 0:
        print("Fizz")
    # Returns 'Buzz' if the argument is divisible by both 3 and 5
    elif x % 5 == 0:
        print("Buzz")
    # Returns the argument itself if it is divisible by both 3 and 5
    else:
        print(x)
