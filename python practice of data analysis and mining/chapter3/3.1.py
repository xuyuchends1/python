import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np

import matplotlib.pyplot as plt
sale_path='E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter3\catering_sale.xls'
sales= pd.read_excel(sale_path,index_col='date')
sales_describe= sales.describe()
sales.boxplot()
plt.show()



