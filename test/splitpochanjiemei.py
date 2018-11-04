fileName="D:\\broke\\s01\\1"
extion=".txt"

list=[]
for line in open(fileName+ extion, encoding="utf-8"):
    print (line)
    a=line.split('\\N',1)
    b= a[1].rsplit('&}',1)
    row=a[0]+"      "+b[1]
    list.append(row)

newfileName=fileName+"_New"
with open(newfileName+ extion, 'w', encoding="utf-8") as f:
    for var in list:
        f.write(var)
