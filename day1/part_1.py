lines = open("input.txt", 'r').readlines()

list1 = []
list2 = []

for line in lines:
	value1, value2 = line.strip().split()
	list1.append(int(value1))
	list2.append(int(value2))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

def find_total_distance(sorted_list1, sorted_list2):
	total_distance = 0
	for i in range(len(list1)):
		total_distance += abs(sorted_list1[i] - sorted_list2[i])
	return total_distance

def main():
 print("Total distance: ", find_total_distance(sorted_list1, sorted_list2))
 
if __name__ == "__main__":
    main()
    