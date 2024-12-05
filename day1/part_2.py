lines = open("input.txt", 'r').readlines()

list1 = []
list2 = []

for line in lines:
	value1, value2 = line.strip().split()
	list1.append(int(value1))
	list2.append(int(value2))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

def calculate_similarity_score(sorted_list1, sorted_list2):
	total_score = 0
	for i in range(len(sorted_list1)):
		similarity_score = 0
		for j in range(len(sorted_list2)):
			if sorted_list1[i] == sorted_list2[j]:
				similarity_score += 1
		total_score += sorted_list1[i] * similarity_score
	
	return total_score

print("Total score: ", calculate_similarity_score(sorted_list1, sorted_list2))