def inverse(dic):
    reverse_dict = {}
    for k, v in dic.items():
            if v in reverse_dict:
                reverse_dict[v].append(k)
            else:
                reverse_dict[v] = [k]
    return reverse_dict
    
dict = {'a': '1', 'b': '2', 'c': '1', 'd': '3', 'e': '1', 'f': '2'}
print(inverse(dict))

