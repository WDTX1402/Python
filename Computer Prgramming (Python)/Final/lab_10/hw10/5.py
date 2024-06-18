def isAnagram(str1,str2):
	if sorted(str1) == sorted(str2):
	 return True
	return False
			
print(isAnagram('silednt', 'listen'))