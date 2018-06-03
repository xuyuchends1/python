import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt


def peak_to_peak(arr):
    return arr.max() - arr.min()


df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'], 'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5), 'data2': np.random.randn(5)})
grouped = df['data1'].groupby(df['key1'])
means = grouped.mean()
means = df['data1'].groupby(df['key1'], df['key2']).mean()
means.unstack()
df.groupby(['key1']).mean()
df.groupby(['key1'])['data1']
people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.ix[2:3, ['b', 'c']] = np.nan
mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f': 'orange'}
by_column = people.groupby(mapping, axis=1)
by_column.sum()

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']
grouped = tips.groupby(['day', 'time'])
grouped.agg(peak_to_peak)
frame = pd.DataFrame({'data1': np.random.randn(1000),'data2': np.random.randn(1000)})
factor=pd.cut(frame.data1, 4)
grouping = pd.qcut(frame.data1, 10, labels=False)