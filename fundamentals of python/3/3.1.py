def indexOfMin(array):
    """return the min value"""
    min_index=0
    current_index=1
    while (current_index<len(array)):
            if (array[current_index]<array[min_index]):
                min_index=current_index
            current_index+=1
    return min_index


def indexOfMin2(array):
    min_index=None
    min_value=None
    for index,value in enumerate(array):
        if min_value == None or value<min_value:
            min_value=value
            min_index=index
    return min_index





min_index= indexOfMin2([4,6,34,1,23,45])

pass


