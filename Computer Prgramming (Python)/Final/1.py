def find_word_positions(word,list_of_words):
	txt = word.lower()
	newlist = []
	for i in list_of_words:
		newlist.append(i.lower())
		
	position = []
	count = 0
	for i in newlist:
		if txt == i:
			position.append(count)
		count += 1
	if len(position) > 0:
		return position
	else:
		position = 0
		return position

word_list = ['python','java','c','PYTHON','Prolog']
			 
print(find_word_positions('python',word_list))