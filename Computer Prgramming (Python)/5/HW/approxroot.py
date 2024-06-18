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