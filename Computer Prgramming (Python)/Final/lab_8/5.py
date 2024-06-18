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