def list_reverse(lis):
    if len(lis) == 0:
        return [] 
    else:
        return [lis.pop()] + list_reverse(lis) 

list1 = [1,2,4,6]
print(list_reverse(list1))

