from collections import defaultdict


class Classifier:
    def __init__(self, bucketPrefix, testBucketNumber, dataFormat):
        self.totals = defaultdict(dict)
        self.prior = {}
        count = 0
        self.format = dataFormat.strip().split('\t')
        # for each of the buckets numbered 1 through 10:
        for i in range(1, 11):
            # if it is not the bucket we should ignore, read in the data
            if i != testBucketNumber:
                filename = "%s-%02i" % (bucketPrefix, i)
                f = open(filename)
                lines = f.readlines()
                f.close()

                for line in lines[1:]:
                    fields = line.strip().split('\t')
                    vector = []
                    for i in range(len(fields)):
                        if self.format[i] == 'attr':
                            vector.append(fields[i])
                        elif self.format[i] == 'class':
                            category = fields[i]
                            self.prior.setdefault(category, 0)
                            self.prior[category] += 1
                            count += 1
                    col = 0
                    for v in vector:
                        col += 1
                        self.totals[category].setdefault(col, {})
                        self.totals[category][col].setdefault(v, 0)
                        self.totals[category][col][v] += 1
        for k, v in self.prior.items():
            self.prior[k] = v / count
        for v1 in self.totals.values():
            for v2 in v1.values():
                for k3, v3 in v2.items():
                    v2[k3] = v3 / count
        pass

    def classify(self, item_vector):
        result = []
        for k, v in self.prior.items():
            value = v
            for k1, v1 in self.totals[k].items():
                if item_vector[k1 - 1] in v1.keys():
                    value *= v1[item_vector[k1 - 1]]
            result.append((value, k))
        return max(result)[1]
        pass


c = Classifier("iHealth/i", 10, "attr\tattr\tattr\tattr\tclass")
print(c.classify(['health', 'moderate', 'moderate', 'yes']))
