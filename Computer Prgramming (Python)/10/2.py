list1 = [3,6,6,3,7,6,2,0,1,5,4]

def remove_the_thirds(inpus):
    to_remove = []
    for i in range(len(inpus)):
        if (i + 1) % 3 == 0:
            to_remove.insert(0, i)

    for i in to_remove:
        inpus.pop(i)

remove_the_thirds(list1)
print(list1)

