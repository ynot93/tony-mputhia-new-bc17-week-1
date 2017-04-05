def data_type(x):
    if type(x) is None:
        return 'no value'
    if type(x) == str:
        return len(x)
    elif type(x) == bool:
        return bool
    elif type(x) == int:
        if x < 100:
            return "less than 100"
        elif x == 100:
            return 'equal to 100'
        else:
            return "more than 100"
    elif type(x) == list:
        if len(x) < 3:
            return None
    else:
        return x[2]
