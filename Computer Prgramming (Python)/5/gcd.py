n1 = int(input("enter"))
n2 = int(input("enter"))

k = 2
gcd = 1
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k ==0:
        gcd = k
    k += 1
print("The greatest common divisor for", n1 , "and", n2, "is", gcd)
