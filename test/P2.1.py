import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
data1 = {1999:5945 ,2000: 5990, 2001: 6085, 2002: 5802,2003:5870}
names1 = list(data1.keys())
values1 = list(data1.values())

data2 = {1999:31536 ,2000: 33312, 2001: 35425, 2002: 40949,2003:45462}
names2 = list(data2.keys())
values2 = list(data2.values())

fig, axs = plt.subplots(1, 2,  sharey=False)
axs[0].bar(names1, values1)
axs[0].set_ylabel("博士学位人数")
axs[0].set_xlabel("年")

axs[1].bar(names2, values2)
axs[1].set_ylabel("博士学位人数")
axs[1].set_xlabel("年")
plt.show()

