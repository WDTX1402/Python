input = int(input("Enter the number of lines:"))

N = input


for i in range(0, (N+1)//2):
    for j in range(i, -1, -1):
        print(2**j, end=" ")
    print()

x = (N//2)

for i in range(0 ,(N+1)//2):
    for j in range(x-1, -1, -1):
        print(2**j, end=" ")
    print()
    x -= 1
    