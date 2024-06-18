text = "abcdefghijk"

s1 = text[5]
print(s1)

s2 = text[1:4]
print(s2)

s3 = text[len(text)-4:len(text)]
print(s3)

s4 = text[::3]
print(s4)

s5 = text[len(text):: -2]
print(s5)

s6 = text[3::3]
print(s6)

s7 = text[0:3].upper()
print(s7)