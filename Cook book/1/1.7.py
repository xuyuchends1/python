# 让字典保存有序
from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 3
d['spam'] = 2
d['grok'] = 4

for key in d:
    print(key, d[key])

print(json.dumps(d))
