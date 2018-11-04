import math
def getAverageSTD(vector):
    average=sum(vector)/len(vector)
    # std=sum(map(lambda x:pow((x-average),2),vector))
    std=sum ([pow((x-average),2) for x in vector])
    std =math.sqrt(std/len(vector))
    return average ,std

def guiyihua(vector):
    average, std=getAverageSTD(vector)
    return [(x-average) / std for x in vector]

value2=guiyihua([75,55,45,115,70,105,69,43])
pass