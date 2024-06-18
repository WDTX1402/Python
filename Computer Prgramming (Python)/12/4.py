def is_subset(sup, sub):
    for i in sub:
        found = False
        for j in sup:
            if i == j:
                found = True
                break
        if not found:
            return False
    return True


sup = set([1,2,3,4])
sub = set([1,2,3])

print(is_subset(sup,sub))