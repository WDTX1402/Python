# def find_member_positions(number,list1):
# 	pos = []
# 	for i in range(len(list1)):
# 		if list1[i] == number:
# 			pos.append(i)
	
# 	if pos == []:
# 		return 0
# 	else:
# 		return pos
	


def find_member_positions(word, list):
    result = []
    for i in range(0, len(list)):
        if word  == list[i]:
            result.append(i)
            

    if result == []:
        return 0
    else:
        return result

print(find_member_positions(2,[2,5,3,2,4]))
print(find_member_positions(1,[2,5,3,2,4]))