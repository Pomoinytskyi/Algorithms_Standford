import random


def Inversion(data):
    dataLength = len(data)
    if(dataLength == 1):
        return ((data, 0))
    return _merge(Inversion(data[:dataLength // 2]), Inversion(data[dataLength // 2:]))


def _merge(leftTup, rightTup):
    # merge two arrays, ordering all elements
    leftLen = len(leftTup[0])
    rightLen = len(rightTup[0])
    result = [None] * (leftLen + rightLen)
    i, j, k = 0, 0, 0
    inversion = 0

    while(i < leftLen and j < rightLen):
        if(leftTup[0][i] < rightTup[0][j]):
            result[k] = leftTup[0][i]
            i += 1
        else:
            result[k] = rightTup[0][j]
            j += 1
            inversion += leftLen - i
        k += 1

    if(i < leftLen):
        result[k:] = leftTup[0][i:]
    else:
        result[k:] = rightTup[0][j:]
    return (result, inversion + leftTup[1] + rightTup[1])


def Main():

    print("============== Inversion counter ==================")
    file = open("./TestData/DevideAndConcure.txt", "r")
    data = []
    for line in file:
        data.append(int(line))
    print("Result:\n{0}".format(Inversion(data)))


if __name__ == "__main__":
    Main()
