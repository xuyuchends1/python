"""从任意长度的可迭代对象中分解元素"""
record=('a','b','c','d')
x,*y,c=record
print (y)

record=('acme',50,123.45,(12,18,2012))
name,*_,(*_,year)=record
print("name: "+name)
print("year: "+str(year))