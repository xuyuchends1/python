import json
from collections import Counter

import functools
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

print("Idioms")
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)

print("if-then")
df.loc[df.AAA >= 5, 'BBB'] = -1
print(df)

df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 555
print(df)

df.loc[df.AAA < 5, ['BBB', 'CCC']] = 2000
print(df)

print("use pandas where after you’ve set up a mask")
df_mask = pd.DataFrame({'AAA': [True] * 4, 'BBB': [False] * 4, 'CCC': [True, False] * 2})
print(df_mask)
df.where(df_mask, -1000)
print(df.where(df_mask, -1000))

print("if-then-else using numpy’s where()")
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
df['logic'] = np.where(df['AAA'] > 5, 'high', 'low')
print(df)

print("Split a frame with a boolean criterion")
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
dflow = df[df.AAA <= 5]
print(dflow)
dfhigh = df[df.AAA > 5]
print(dfhigh)

print("Select with multi-column criteria")
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA']
print(newseries)
df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1
print(df)

print("Idioms")
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
aValue = 43.0
print("Select rows with data closest to certain value using argsort")
newdf=df.loc[(df.CCC - aValue).abs().argsort()]
print(newdf)

print("Dynamically reduce a list of criteria using a binary operators")
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
Crit1 = df.AAA <= 5.5
Crit2 = df.BBB == 10.0
Crit3 = df.CCC > -40.0
CritList = [Crit1,Crit2,Crit3]
AllCrit = functools.reduce(lambda x,y: x & y, CritList)

print("DataFrames")
print("Using both row labels and value conditionals")
df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]})
newdf=df[(df.AAA <= 6) & (df.index.isin([0,2,4]))]
print(newdf)

print("Use loc for label-oriented slicing and iloc positional slicing")
data = {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}
df = pd.DataFrame(data=data,index=['foo','bar','boo','kar'])
print(df)
newdf=df.loc['bar':'kar']
print(newdf)
newdf=df.iloc[0:3]
print(newdf)

#Ambiguity arises when an index consists of integers with a non-zero start or non-unit increment.
df2 = pd.DataFrame(data=data,index=[1,2,3,4])
newdf=df2.iloc[1:3]#Position-oriented
print(newdf)
newdf=df2.loc[1:3]#Label-oriented
print(newdf)

print("Using inverse operator (~) to take the complement of a mask")
df = pd.DataFrame( {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40], 'CCC' : [100,50,-30,-50]})
newdf=df[~((df.AAA <= 6) & (df.index.isin([0,2,4])))]
print(newdf)

print("Extend a panel frame by transposing, adding a new dimension, and transposing back to the original dimensions")
rng = pd.date_range('1/1/2013',periods=100,freq='D')
data = np.random.randn(100, 4)
cols = ['A','B','C','D']
print(rng)
print(data)
print(cols)
df1, df2, df3 = pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols)
pf = pd.Panel({'df1':df1,'df2':df2,'df3':df3})
pf.loc[:,:,'F'] = pd.DataFrame(data, rng, cols)

print("Efficiently and dynamically creating new columns using applymap")
df = pd.DataFrame({'AAA' : [1,2,1,3], 'BBB' : [1,1,2,2], 'CCC' : [2,1,3,1]})
source_cols = df.columns # or some subset would work too.
new_cols = [str(x) + "_cat" for x in source_cols]
categories = {1 : 'Alpha', 2 : 'Beta', 3 : 'Charlie' }
df[new_cols] = df[source_cols].applymap(categories.get)
print(df)

print("Keep other columns when using min() with groupby")
df = pd.DataFrame( {'AAA' : [1,1,1,2,2,2,3,3], 'BBB' : [2,1,3,4,5,1,2,3]})
print("idxmin() to get the index of the mins")
newdf=df.loc[df.groupby("AAA")["BBB"].idxmin()]
#根据AAA分组,找最小BBB的index
print(newdf)

print("sort then take first of each")

newdf=df.sort_values(by="BBB").groupby("AAA", as_index=False).first()
print(newdf)

print("Creating a multi-index from a labeled frame")
df = pd.DataFrame({'row' : [0,1,2],'One_X' : [1.1,1.1,1.1],'One_Y' : [1.2,1.2,1.2],'Two_X' : [1.11,1.11,1.11],'Two_Y' : [1.22,1.22,1.22]})
print(df)
df = df.set_index('row')
print(df)

print("# With Hierarchical Columns")
df.columns = pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df.columns])
print(df)

df = df.stack(0).reset_index(1)
print(df)
df.columns = ['Sample','All_X','All_Y']
print (df)

print("Performing arithmetic with a multi-index that needs broadcasting")
cols = pd.MultiIndex.from_tuples([ (x,y) for x in ['A','B','C'] for y in ['O','I']])
df = pd.DataFrame(np.random.randn(2,6),index=['n','m'],columns=cols)
print (df)

print("Slicing a multi-index with xs")
coords = [('AA','one'),('AA','six'),('BB','one'),('BB','two'),('BB','six')]
index = pd.MultiIndex.from_tuples(coords)
df = pd.DataFrame([11,22,33,44,55],index,['MyData'])
print(df)

print("To take the cross section of the 1st level and 1st axis the index:")

df.xs('BB',level=0,axis=0) #Note : level and axis are optional, and default to zero
print (df)