def power(inpus):
    power_set = [[]]
    for i in inpus:
        new_subsets = [list(j) + [i] for j in power_set]
        power_set.extend(new_subsets)

    setttt = set()
    for j in power_set:
        setttt.add(frozenset(j))

    return setttt


s = ([1, 2, 3])
print(power(s))

# def powerset(lst):
#     power = [[]]
#     for i in set(lst):
#         power += [x +[i] for x in power]
#     return power

# print(powerset(s))