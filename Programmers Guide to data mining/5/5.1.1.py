


class Classifier():
    def __init__(self,bucketPrefix, dataFormat,skipIndex=0):
        self.data=[]
        self.classTypes = []
        self.format = dataFormat.strip().split('\t')
        for i in range(1, 11):
            if i!=skipIndex:
                filename = "%s-%02i" % (bucketPrefix, i)
                f = open(filename)
                lines = f.readline()
                f.close()
                for line in lines[1:]:
                    fields = lines.strip().split('\t')
                    vector = []
                    classType = []
                    for j in range(len(fields)):
                        if self.format[j] == 'num':
                            vector.append(fields[j])
                        elif self.format[j] == 'class':
                            self.classTypes.append(fields[j])
                    self.data.append(vector)

        pass
    pass



def tenfold(bucketPrefix,dataFormat,knn):
    for i in range(1,11):
        Classifier(bucketPrefix,dataFormat,i)
        filename = "%s-%02i" % (bucketPrefix, i)
        f=open(filename)
        lines =  f.readline()
        f.close()
        # for line in lines[1:]:
        #     fields=line.strip().split('\t')
        #     for i in range(len(fields)):
        #         if dataFormat[i]=='num':






    pass


print("SMALL DATA SET")
tenfold("pimaSmall/pimaSmall",
        "num	num	num	num	num	num	num	num	class", 3)
print("\n\nLARGE DATA SET")









