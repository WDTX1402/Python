def popularity_scores(language_scores):
  
	sorted_scores = sorted(language_scores.items(), key=lambda item: item[1], reverse=True)
	ranked_languages = {}
	current_rank = 1
	last_score = None
  
	for language, score in sorted_scores:
		if score == last_score:
	
			ranked_languages[language] = current_rank - 1
		else:
 
			ranked_languages[language] = current_rank
			last_score = score
		current_rank += 1

   
	result = {}
	for language, rank in ranked_languages.items():
		if rank not in result:
			result[rank] = language
		else:
			result[rank] += ", " + language

	return result

pop = {'C++': 99.7, 'C': 96.7, 'Java': 97.5, 'Python': 100, 'C#': 89.4, 'Ruby': 97.5}





dick1 = {
    "c++": 99.7,
    "C": 99.7,
    "Java": 97.5,
    "Python": 5,
    "C#": 89.4
    }
sortedlist = []

for v in dick1.values():
    if(v not in sortedlist):
        sortedlist.append(v)

sortedlist.sort(reverse=True)

dick2 = {}
ranking = 1
for rank in sortedlist:
    fuck = ""
    for k,v in dick1.items():
        if v == rank:
            if(len(fuck) > 0):
                fuck += ","
            fuck += k
    dick2[str(ranking)] = fuck
    ranking += 1
print(dick2)
        
