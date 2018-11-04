import pandas as pd
filename='sales_data.xls'
data=pd.read_excel(filename,index_col = u'序号')

data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:,:3].astype(int)
y = data.iloc[:,3].astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn import tree
dtc=DTC(criterion='entropy')
dtc.fit(x,y)

#导入相关函数，可视化决策树。
#导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
from sklearn.tree import export_graphviz
x = pd.DataFrame(x)
from sklearn.externals.six import StringIO
x = pd.DataFrame(x)
with open("tree.dot", 'w') as f:
  f = export_graphviz(dtc, feature_names = x.columns, out_file = f)

pass