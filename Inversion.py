import random

def Inversion(data):
#Merge sort algorithm implementation
	dataLength = len(data)
	if(dataLength == 1):
		return (data, 0)
	return _merge(
		Inversion(data[:dataLength // 2]),
		Inversion(data[dataLength // 2:]))

def _merge(left, right):
#merge two arrays, ordering all elements
	leftLen = len(left[0])
	rightLen = len(right[0])
	result = [None] * (leftLen + rightLen)
	i , j, k = 0, 0, 0
	previousInserted = (1 == 1)
    # False - left(i), True - right(j)
	inversion = 0

	while(i < leftLen and j < rightLen):
		if(left[0]][i] < right[0][j]):
			result[k] = left.data[i]
			i+=1
            if(previousInserted):
                inversion += 1                
            previousInserted = False
		else:
			result[k] = right[0][j]
			j+=1
            previousInserted = True

		k+=1
	
	result[k:] = left[0][i:] if(i < leftLen) else right[0][j:]
	return (result, inversion + left.inv + right.inv)

def Inversion():
    

def Main():
    print("============== Inversion counter ==================")
    data = random.sample(range(0, 10), 10)
    print("Initial data:\n{0}".format(data))
    print("Result:\n{0}".format(Inversion(data)))

if __name__== "__main__":
    Main()
    