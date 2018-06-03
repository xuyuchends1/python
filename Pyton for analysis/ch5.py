import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

s1:pd.Series = pd.Series([7.3,-2.5,3.4,1.5],index=['a','b','c','d'])
s2=pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
s3=s1+s2
s3=s1.add(s2,fill_value=0)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df3=df1.add(df2, fill_value=0)

arr=np.arange(12).reshape(3,4)
arr2=arr-arr[0]

frame =pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series=frame.iloc[0]
series3=frame['d']
frame.sub(series3,axis=0)

df1=pd.DataFrame({'key':['b','b','a','c','a','a','b'], 'data1':range(7)})
df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
pd.merge(df1,df2)

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
   periods=10), columns=list('ABCD'))

fig,axes=plt.subplots(2,1)
data=pd.Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(kind='barh',ax=axes[0],color='k',alpha=0.7)
data.plot(kind='bar',ax=axes[1],color='k',alpha=0.7)
plt.show()