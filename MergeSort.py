import random

def MergeSort(data):
#Merge sort algorithm implementation
	dataLength = len(data)
	if(dataLength == 1):
		return data
	return _merge(
		MergeSort(data[:dataLength // 2]),  
		MergeSort(data[dataLength // 2:]))

def _merge(left, right):
#merge two arrays, ordering all elements
	leftLen = len(left)
	rightLen = len(right)
	result = [None] * (leftLen + rightLen)
	i , j, k = 0, 0, 0

	while(i < leftLen and j < rightLen):
		if(left[i] < right[j]):
			result[k] = left[i]
			i+=1
		else:
			result[k] = right[j]
			j+=1

		k+=1
	
	result[k:] = left[i:] if(i < leftLen) else right[j:]
	return result

print("\n=====================\nMergeSrot algorith:")
data = random.sample(range(-10, 10), 10)
print("Initial data:\n{0}".format(data))
print("Result:\n{0}".format(MergeSort(data)))
