list1 = [3,1,1,1,2,7]
list2 = [4,1,1,2,2,5]

def get_the_difference(ls1,ls2):
    munsum = []
    in1 = [i for a,i in enumerate(ls1)]
    in2 = [i for a,i in enumerate(ls2)]
    for i in in1:
        for j in in2:
            if i == j:
                munsum.append(i)
    
    for i in munsum:
        if i in in1:
            in1.remove(i)
        if i in in2:
            in2.remove(i)
    
    byebye = in1 + in2

    return byebye

k = get_the_difference(list1,list2)
print(k)
print(list1)
print(list2)