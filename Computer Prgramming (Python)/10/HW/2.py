def bubble_sort(listin):
    length = len(listin)
    
    for i in range(length):
        swaps = 0
        for i in range(0, length - 1):
            if listin[i] > listin[i + 1]:
                listin[i], listin[i + 1] = listin[i + 1], listin[i]
                swaps += 1
        if swaps == 0:
            break
        length -= 1

    return listin

list = [3,2,9,7,8]
out = bubble_sort(list)
print(out)
