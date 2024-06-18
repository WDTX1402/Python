def perm2(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if i != j:
                print((t[i], t[j]), end = '')

def perm3(t):
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if i != j and i != k and j != k:
                    print((t[i], t[j], t[k]))

def perm(t, n):
    if n == 0:
        return [()]
    
    if not t:
        return []

    result = []
    for i in range(len(t)):
        rest = perm(t[:i] + t[i+1:], n-1)
        for p in rest:
            result.append((t[i],) + p)
    return result

def print_perm(t, n):
    for p in perm(t, n):
        print(p, end = '')

#perm2((1,2,3))
#print('\n')
#perm3((1,2,3,4))
#print('\n')
print_perm((1,2,3),3)
