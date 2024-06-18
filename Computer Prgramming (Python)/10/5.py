list1 = [1,5,16,61,111]
list2 = [2,4,5,6]

list3 = [1,1,1,1,8,8,8,8,15,15,15,15]
list4 = [2,4,6,8,10]


def merge(ls1,ls2):
    output = []
    if len(ls1) >= len(ls2):
        long = ls1
        short = ls2
    else:
        long = ls2
        short = ls1
    
    i = 0
    j = 0
    
    while j in range(0,len(short)):
        if long[i] > short[j]:
            output.append(short[j])
            j += 1
        elif long[i] < short[j]:
            output.append(long[i])
            i += 1
        else:
            output.append(long[i])
            output.append(short[j])
            i += 1
            j += 1
            
    while i < len(long):
        output.append(long[i])
        i += 1
       

    realoutput = (f"The merged list is{output}")

    return realoutput

k = merge(list3,list4)
print(k)
g = merge(list1,list2)
print(g)