#Q1
def print_btree(tree, dpt=0):
    if isinstance(tree,int):
        print("." * dpt + str(tree))
    else:
        print("." * dpt + str(tree[0]))
        if len(tree) >= 1:
            for child in tree[1]:
                print_btree(child,dpt + 1)

tree = [1,[[11, [111, 112]],[12, [121, [122, [1221, 1222]]]]]]

print_btree(tree)


#Q2
def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 1:  
        return 0

    return 2 * f(n // 2) + 1

def display_f(n):
    for i in range(n+1):
        print(f(i))

display_f(5)

#Q3
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
                    print((t[i], t[j], t[k]), end = '')

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

perm2((1,2,3))
print('\n')
perm3((1,2,3,4))
print('\n')
print_perm((1,2,3),3)


#Q4


#Q5
import turtle as t

t.left(90)
t.tracer(0)

def tree(input):
    if input < 10:
        return
    else:
        t.fd(input)
        t.left(30)
        tree((3*input)/4)
        t.right(60)
        tree((3*input)/4)
        t.left(30)
        t.back(input)

tree(100)
t.done()
