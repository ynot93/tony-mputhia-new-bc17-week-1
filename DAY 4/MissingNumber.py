def find_missing(l_one, l_two):
    if l_one == 0 and l_two == 0:
        return 0
        pass
    s_one = set(l_one)
    s_two = set(l_two)

    print(list(s_one ^ s_two))

# test case
# find_missing([1, 2, 3], [1, 2, 3, 4])
