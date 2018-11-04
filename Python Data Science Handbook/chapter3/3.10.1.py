import pandas as pd
import numpy as np
import seaborn as sns
t=population_path = 'E:\phil\workspace\selfwork\python\Python Data Science Handbook\chapter3\\titanic.csv'
t=pd.read_csv(t)
t.groupby(['sex','class']).mean()
t.groupby(['sex','class'])['survived'].mean()
t.groupby(['sex','class'])['survived'].mean().unstack()
t.pivot_table('survived',index='sex',columns='class')