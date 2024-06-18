dict1 = {}
dict2 = {}
def composite(dict1, dict2):
    dict3 = {}
    for k1, v1 in dict1.items():
        for k2,v2 in dict2.items():
            if v1 == k2:
                dict3[k1] = v2

    return dict3


dict1 = {'a':'p', 'b':'r', 'c':'q', 'd':'p', 'e':'s'}
dict2 = {'p':'1','q':'2','r':'3'}

print(composite(dict1, dict2))