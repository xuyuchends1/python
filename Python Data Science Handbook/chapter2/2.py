import numpy as np

l=list(range(10))
type(l)
l2=[str(c) for c in l]
# defuault  dtype=float64
np.zeros(10,dtype=int)
np.ones((3,5))
np.full((3,5),3.14)
np.arange(0,20,3)
np.linspace(0,1,5)
np.random.random((3,5))
np.random.normal(0,1,(3,3))
np.random.randn((3,3))
np.random.randint(0,10,(3,3))
np.eye(3)
np.empty(3)
x=np.array([1,2,3])
y=np.array([3,2,1])
np.concatenate(x,y)