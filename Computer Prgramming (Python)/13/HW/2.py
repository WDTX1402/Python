def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 1:  
        return 0

    return 2 * f(n // 2) + 1

def display_f(n):
    for i in range(n+1):
        print(f(i))

display_f(3)