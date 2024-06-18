def isAnagram(string1, string2):
    count1 = {}
    for char in string1:
        count1[char] = count1.get(char, 0) + 1
    
    count2 = {}
    for char in string2:
        count2[char] = count2.get(char, 0) + 1

    if count1 == count2:
        return "True"
    else:
        return "False"

word1 = "listen"
word2 = "silent"
out1 = isAnagram(word1, word2)
print(out1)

word1 = "hello"
word2 = "helnaw"
out2 = isAnagram(word1, word2)
print(out2)
