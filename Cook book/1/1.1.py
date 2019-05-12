"""将序列分解成单独的变量"""
p=(4,5)
x,y=p
print (x)
print(y)

data=['acme',50,91.1,(2012,12,21)]
a,b,c,(d,e,f)=data
print ("a="+a)
print ("b="+str(b))
print ("c="+str(c))
print ("d="+str(d))
print ("e="+str(e))
print ("f="+str(f))
