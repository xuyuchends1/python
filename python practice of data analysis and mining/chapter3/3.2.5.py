#贡献度分析
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

sale_path = 'E:\phil\workspace\selfwork\python\python practice of data analysis and mining\chapter3\catering_dish_profit.xls'
data = pd.read_excel(sale_path, index_col='菜品名', usecols  =[1,2])
data['累计比例']=data.cumsum()/data.sum()
#secondary_y 右侧Y
p1= data['累计比例'].plot(linestyle='dashed', color='r', marker='o' ,secondary_y=True)
p1.set_ylabel('累计比例')

# 添加注释
# 第一个参数是注释的内容
# xy设置箭头尖的坐标
# xytext设置注释内容显示的起始位置
# arrowprops 用来设置箭头
# facecolor 设置箭头的颜色
# headlength 箭头的头的长度
# headwidth 箭头的宽度
# width 箭身的宽度
plt.annotate(format(data['累计比例'][6],'.4%'), xy = (6, data['累计比例'][6]), xytext = (7, data['累计比例'][6]),
             arrowprops = dict(arrowstyle="->"))

p2=data['盈利'].plot.bar()
p2.set_ylabel('盈利')
plt.show()