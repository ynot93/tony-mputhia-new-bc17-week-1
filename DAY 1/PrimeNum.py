class CalcPrime(object):
    def __init__(self):
        self.number = int(input("Find prime numbers up to : "))

        isprime = True
        for x in range(2, self.number + 1):

            for y in range(2, int(x**0.5)+1):
                if x % y == 0:
                    isprime = False
                    break

            if isprime:
                print(x)


