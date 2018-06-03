import json
from pandas.core.algorithms import value_counts
from spyder.pyplot import barh
from collections import Counter
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dict = []
# with open("example.txt","r") as f:
#     for line in f.readlines():
#        dict.append(str(json.loads(line)))

records = [json.loads(line) for line in open("source\\example.txt", "r")]
print(records[0])
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = Counter(time_zones)
counts.most_common(5)
print("counts.most_common(5)")
print(counts.most_common(5))

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
print ("tz_counts")
print(tz_counts)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == '']='Unknown'
tz_counts =clean_tz.value_counts()[0:10]
print ("tz_counts")
print (tz_counts)
print (tz_counts._values)

plt.show(tz_counts.plot(kind='barh', rot=1))