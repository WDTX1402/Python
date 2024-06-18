print("Pattern A")
N = 6
for i in range(1, N-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n")

print("Pattern B")
x = N
for i in range(1, N):
    for j in range(1, x):
        print(j, end=" ")
    print()
    x -= 1
