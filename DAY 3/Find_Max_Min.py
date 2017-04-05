def find_max_min():
    entry = [int(x) for x in input('Enter a list of numbers : ').split()]

    while entry != '':
        entry.sort()
        break
    print([entry[0], entry[1]])

find_max_min()
