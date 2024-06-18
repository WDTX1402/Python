#Q1
import math

n = int(input("Enter a number:"))

result = math.sqrt(n)

guess = n/2

for j in range(8):
         temp = n/guess
         guess = (guess  + temp)/2
         if j == 5 or j == 6 or j == 7: 
              print("The approximate square root value of", n ,"when iterated", j ,"times is", format(guess, '.3f'))

print("The actual square root of", n , "is" ,format(result, '.3f'))

#Q2
# :(
    
#Q3
while True:
    print()
    inpus = input("Enter a number: ")

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
 