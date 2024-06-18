def find_word_positions(word,list1):
	wrd = word.lower()
	lst = []
	for i in list1:
		lst.append(i.lower())
	
	result = []
	for i in range(len(lst)):
		if wrd == lst[i]:
			result.append(i)
	
	if result == []:
		return 0
	else:
		return result
	
print(find_word_positions('Python',['python','java', 'c','PYTHON','Prolog']))
print(find_word_positions('iOS',['Windows','macOS','Linux']))
