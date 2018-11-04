#有监督学习
#线性回归
import matplotlib.pyplot as plt
import numpy as np
rng=np.random.RandomState(42)
x=10*rng.rand(50)
y=2*x-1+rng.randn(50)
fig=plt.figure()
ax=plt.axes()
ax.plot(x,y,'o')

from sklearn.linear_model import LinearRegression
model=LinearRegression(fit_intercept=True)
X=x[:,np.newaxis]
model.fit(X,y)
x1=1
y1=x1*model.coef_+ model.intercept_
x2=10
y2=x2*model.coef_+ model.intercept_

ax.plot([x1,x2],[y1,y2])

plt.show()

#有监督学习
#高斯分类

from sklearn.naive_bayes import GaussianNB
import seaborn as sns
iris=sns.load_dataset('iris')
iris.to_csv('1.csv')


