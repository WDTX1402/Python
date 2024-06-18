def name_list():
    name = []
    i = 1
    while True:
        inpus = str(input(f"Enter name {i}: "))
        if len(inpus) == 0:
            break
        else:
            name.append(inpus)
        i += 1
    return name

    
k = name_list()
print(k)