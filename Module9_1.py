def apply_all_func(int_list, *functions):
    reuslts = {}
    for i in functions:
        reuslts[i.__name__] = i(int_list)
    return reuslts

int_list = [6, 20, 15, 9]

print(apply_all_func(int_list, len, sum, sorted, max, min))