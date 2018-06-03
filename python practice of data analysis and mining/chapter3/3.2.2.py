import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

sale_path="catering_dish_profit.xls"
sales= pd.read_excel(sale_path,index_col=u'菜品名',usecols =[1,2])
menu_sales= sales.sort_values(by=[u'盈利'],ascending=False)
menu_sales.head(5)
menu_sales.head(5).plot.pie(y = u'盈利')
plt.show()
menu_sales.head(5).plot.bar()
plt.show()