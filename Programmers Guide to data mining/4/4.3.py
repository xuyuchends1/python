import math
def calcMedian(a):
    array=list(a)
    array.sort()
    if len(array)%2==0:
        half_index=int(len(array)/2-1)
        return (a[half_index]+a[half_index+1])/2
    else:
        half_index=int(len(array)/2)
        return a[half_index]

def getSTD(vector,median):
    std=sum ([abs(x-median) for x in vector])
    std =std/len(vector)
    return std

def getMMS(vector,median,std):
    return [(x-median)/std for x in vector]

vector1=[43,45,55,69,70,75,105,115]
median1=calcMedian(vector1)
std=getSTD(vector1,median1)

vector2=[21,15,12,3,7]
median2=calcMedian(vector2)
std2=getSTD(vector2,median2)
mms2=getMMS(vector2,median2,std2)
pass