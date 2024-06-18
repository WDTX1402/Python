def find_duplicates(d):
    dup = {}
    for i1, j1 in d.items():
        for i2, j2 in d.items():
            if i1 != i2 and j1 == j2:
                dup[i1] = j1
                break
    return dup

dict_example = {
    's5301': 'Fred',
    's5302': 'Harry',
    's5303': 'John',
    's5304': 'Fred',
    's5305': 'Harry',
}

print(find_duplicates(dict_example))

