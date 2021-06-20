# Problem Statement:
# Write a function that takes in an array of unique integers and returns an
# array of all permutations of those integers in no particular order.
# If the input array is empty, the function should return an empty array.

def permutations(list):
    if list == [] or len(list) == 1:
        return [list]
    else:
        sub = []
        ret_list = []
        for i in range(len(list)):
            list[0],list[i] = list[i],list[0] #swapping 1st element with ith element
            sub = permutations(list[1:len(list)])
            ret_list = ret_list + [[list[0]]  + sub[j] for j in range(len(sub))]
        return ret_list

print(permutations([1,2]))

'''def powerset(original, newset):
	if original == []:
		return [newset]
	else:
		res = []
		for s in powerset(original[1:], newset+[original[0]]):
			res.append(s)
		for s in powerset(original[1:], newset):
			res.append(s)
		return res

print(powerset([1,2,3], []))'''