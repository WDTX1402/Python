def product(*sets):
    if not sets:
        return set([])
    if len(sets) == 1:
        return set([(item,) for item in sets[0]])
    
    sub_product = product(*sets[1:])
    cartesian = [(item,) + tuple_ for item in sets[0] for tuple_ in sub_product]
    return set(cartesian)

s1 = set([1,2,3])
s2 = set(['p','q'])
s3 = set(['a','b','c'])
print(product(s1,s2))
print(product(s1, s2, s3))
print(product(s1))