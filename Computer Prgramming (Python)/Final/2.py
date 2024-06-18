def popularity_scores(input_dict):
	ranked = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
	rank = 1
	result = {}
	prev_score = None
	for language, score in ranked:
		if score == prev_score:
			result[language] = rank
		else:
			result[language] = rank
			rank += 1
		prev_score = score
	
	return result

pop = {'C++': 99.7, 'C': 96.7, 'Java': 97.5, 'Python': 100, 'C#': 89.4, 'Ruby': 97.5}
print(popularity_scores(pop))

# def popularity_scores(inpus):
#	 swap = {}
#	 for v,k in inpus.items():
#		 swap[v] = k
#	 ranked = sorted(swap.items(), key=lambda x:x[1])
#	 rankeddict = dict(ranked)
#	 pos = 1
#	 for v,k in rankeddict.items():
#		 ranked[v] = pos
#		 pos += 1
#	 return ranked


		
# pop = {'C++':99.7 ,'C': 96.7 ,'Java': 97.5 ,'Python':100 ,'C#': 89.4}

# print(popularity_scores(pop))

# def rank_languages(popularity_scores):
#	 result = {}
#	 temp_scores = popularity_scores.copy() 
#	 rank = 1

#	 while temp_scores:
#		 highest_language = max(temp_scores, key=temp_scores.get)
#		 highest_score = temp_scores[highest_language]

#		 result[rank] = highest_language
#		 del temp_scores[highest_language]

#		 rank += 1

#	 return result

# # Example usage:
# popularity_scores = {"C++": 99.7, "C": 96.7, "Java": 97.5, "Python": 100, "C#": 89.4}
# result = rank_languages(popularity_scores)
# print(result)
