import math
import sys
from collections import defaultdict
class Classifier:

    def __init__(self, filename):

        self.medianAndDeviation = []

        # reading the data in from the file
        f = open(filename)
        lines = f.readlines()
        f.close()
        self.format = lines[0].strip().split('\t')
        self.data = []
        num_list=defaultdict(list)
        for line in lines[1:]:
            num_index = 0
            fields = line.strip().split('\t')
            ignore = []
            vector = []
            for i in range(len(fields)):
                if self.format[i] == 'num':
                    vector.append(int(fields[i]))
                    num_list[num_index].append(int(fields[i]))
                    num_index+=1
                elif self.format[i] == 'comment':
                    ignore.append(fields[i])
                elif self.format[i] == 'class':
                    classification = fields[i]

            # median=self.getMedian(vector)
            # std=self.getAbsoluteStandardDeviation(vector,median)
            self.data.append((classification, vector, ignore))

        self.rawData = list(self.data)
        self.tong_ji_liang={}
        for k,v in num_list.items():
            median=self.getMedian(v)
            asd=self.getAbsoluteStandardDeviation(v,median)
            self.tong_ji_liang[k]=[median,asd]


        for _,array,_ in self.data:
            for index,value in enumerate(array):
                median=self.tong_ji_liang[index][0]
                asd=self.tong_ji_liang[index][1]
                array[index]=(array[index]-median)/asd
        pass


    def getMedian(self,vector):
        array = list(vector)
        array.sort()
        if len(array) % 2 == 0:
            half_index = int(len(array) / 2 - 1)
            return (array[half_index] + array[half_index + 1]) / 2
        else:
            half_index = int(len(array) / 2)
            return array[half_index]

    def getAbsoluteStandardDeviation(self,vector,median):
       return sum([abs(x-median) for x in vector])/len(vector)

    def getManHanDunDistance(self,vector1,vector2):
        return sum(map(lambda x1,x2:abs(x1-x2),vector1,vector2))

    def nerestNeighbor(self,newVector):
        for index,value in enumerate(newVector):
            median=self.tong_ji_liang[index][0]
            asd=self.tong_ji_liang[index][1]
            newVector[index]=(value-median)/asd

        min=sys.float_info.max
        for item in self.data:
            distance=self.getManHanDunDistance(item[1],newVector)
            if distance<min:
                min=distance
                type=item[0]
        return type
        pass



def unitTest():
    list1 = [54, 72, 78, 49, 65, 63, 75, 67, 54]
    list2 = [54, 72, 78, 49, 65, 63, 75, 67, 54, 68]
    list3 = [69]
    list4 = [69, 72]
    classifier = Classifier('athletesTrainingSet.txt')
    class_type= classifier.nerestNeighbor([70,170])
    class_type = classifier.nerestNeighbor([59, 90])

    m1 = classifier.getMedian(list1)
    m2 = classifier.getMedian(list2)
    m3 = classifier.getMedian(list3)
    m4 = classifier.getMedian(list4)

    asd1 = classifier.getAbsoluteStandardDeviation(list1, m1)
    asd2 = classifier.getAbsoluteStandardDeviation(list2, m2)
    asd3 = classifier.getAbsoluteStandardDeviation(list3, m3)
    asd4 = classifier.getAbsoluteStandardDeviation(list4, m4)

    assert (round(m1, 3) == 65)
    assert (round(m2, 3) == 66)
    assert (round(m3, 3) == 69)
    assert (round(m4, 3) == 70.5)

    assert(round(asd1, 3) == 8)
    assert(round(asd2, 3) == 7.5)
    assert(round(asd3, 3) == 0)
    assert(round(asd4, 3) == 1.5)

unitTest()