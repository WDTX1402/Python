while True:
    print()
    inpus = input("Input: ")

    if inpus == 'exit':
        break

    try:
        e = int(inpus)
    except ValueError:
        continue

    if e >= 1:
        n = 0 
        for r in range(0, e):
            e -= 1 
            for x in range(0, e+1):
                n = n + 1
                for a in range (0, n-1):
                    print('*', end='')
                print()
            for b in range(0, e + 1):
                n = n - 1
                if b == e:
                    print('*', end = '')
                else:
                 for d in range (0, n+1):
                    print('*', end='')
                 print()
    else:
        continue
 