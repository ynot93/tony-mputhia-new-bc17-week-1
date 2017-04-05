num = int(input("Find prime numbers up to : "))

isPrime = True
for x in range(2, num+1):

    for y in range(2, x):
        if x % y == 0:
            isPrime = False
            break

    if isPrime:
        print(x)
