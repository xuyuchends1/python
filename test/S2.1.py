import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
data = {'煤矿崩塌': 7, '溃坝': 4, '煤气爆炸': 28, '闪电': 1,'核反应堆':1,'燃油火灾':4}
names = list(data.keys())
values = list(data.values())

axs = plt.subplot()
axs.bar(names, values)
axs.set_xlabel("原因")
plt.show()