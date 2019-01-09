def indexOfMin(array):
    """return the min value"""
    min_index = 0
    current_index = 1
    while (current_index < len(array)):
        if (array[current_index] < array[min_index]):
            min_index = current_index
        current_index += 1
    return min_index


def indexOfMin2(array):
    min_index = None
    min_value = None
    for index, value in enumerate(array):
        if min_value == None or value < min_value:
            min_value = value
            min_index = index
    return min_index


min_index = indexOfMin2([4, 6, 34, 1, 23, 45])

def binarySearch(target, sortedList):
    """二叉树查询'"""
    left = 0
    right = len(sortedList)
    while left <= right:
        midpoint = (left + right) // 2
        if sortedList[midpoint] == target:
            return midpoint
        elif sortedList[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    else:
        return -1

index = binarySearch(4, [1, 2, 3, 4, 5, 6, 7, 8, 9])

def selectionSort(lyst):
    """选择排序"""
    i=0
    while i<len(lyst)-1:
        j=i+1
        min_value = lyst[i]
        min_index=i
        while j<len(lyst):
            if lyst[j]<min_value:
                min_value=lyst[j]
                min_index=j
            j+=1
        if min_index!=i:
            lyst[i],lyst[min_index]=min_value,lyst[i]

        i+=1

lyst=[5,3,1,2,4]
index = selectionSort(lyst)


def bubbleSort(lyst):
    """冒泡排序"""



pass
