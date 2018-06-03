#随机漫步
import numpy as np

nstep=1000
draws=np.random.randint(0,2,size=nstep)
steps=np.where(draws>0,1,-1)
walk=steps.argmax().cumsum()
print (walk)
print (walk.min())
print (walk.max())