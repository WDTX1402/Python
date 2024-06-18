def LCS1(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

print(LCS1("ingenious", "intelligent")) 


# def LCS(s1, s2):
#     m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
#     longest = 0
#     end_index = 0

#     for i in range(1, len(s1) + 1):
#         for j in range(1, len(s2) + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 m[i][j] = m[i - 1][j - 1] + 1
#                 if m[i][j] > longest:
#                     longest = m[i][j]
#                     end_index = i

#     start_index = end_index - longest
#     return s1[start_index:end_index]

# # Test the function
# result = LCS("ingenious", "intelligent")
# print(result)  # Output: "gen"

def LCS(s1,s2):
    if s1 < s2 :
        short = s1
        long = s2
    else :
        short = s2
        long = s1
    s = 0
    ans = ""
    for i in range(len(long)+1):
        if long[s:i] in short:
            ans = long[s:i]
        else :
            s += 1
    return ans

print(LCS("ingeneious","intelligent"))
print(LCS("philosophically","zoophilous"))
print(LCS("intelligent","inconsidered"))
print(LCS("russian","ukrainian"))
print(LCS("war","love"))
print(LCS("romanian","rominiranian"))