def reverse(x):
    xx = str(x)
    return xx[3] + xx[2] + xx[1] + xx[0]  

komp = reverse(3456)
print(komp)

def reverse2(x):
    xx = str(x)
    
    return xx[:: -1] 


komp = reverse(3456) , reverse2(3456)
print(komp)