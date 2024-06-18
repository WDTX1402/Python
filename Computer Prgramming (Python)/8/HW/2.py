x = input("Enter some text: ")

len = len(x)

char_count = {}

for i in x:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
    print(char_count)

print("-- Character Frequency Table --")

for char, count in char_count.items():
    percent= (count / len) * 100
    print(f"{char} = {percent:.2f}%")
