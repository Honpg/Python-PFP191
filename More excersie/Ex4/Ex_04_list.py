def inp_array():
    inp = input('Enter a number: ')
    Max = int(inp)
    Min = int(inp)

    while inp != 'done':
        inp = input('Enter a number: ')
        if inp.isdigit():
            Max = max(int(inp), Max)
            Min = min(int(inp), Min)
    return Max, Min

max, min = inp_array()
print(f'''Maximum: {max}
Minimum: {min}''')

