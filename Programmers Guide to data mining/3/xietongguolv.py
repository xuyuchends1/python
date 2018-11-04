import math
users3 = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Matt":  {"Imagine Dragons": 3, "Daft Punk": 4,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Ben":   {"Kacey Musgraves": 4, "Imagine Dragons": 3,
                    "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
                    "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori":  {"Kacey Musgraves": 5, "Imagine Dragons": 4,
                    "Daft Punk": 5, "Fall Out Boy": 3}}

def calcxiangsidu(x,y,users:dict):
    x_y = []
    user_average = {}

    for key,value in users.items():
        average = sum(value.values()) / len(value.values())
        user_average[key] = average

        if x in value.keys() and y in value.keys():
            x_y.append((value[x]-user_average[key] ,value[y]-user_average[key] ))
    fen_zi = 0
    fen_wu_zuo = 0
    fen_wu_you = 0
    for item in x_y:
        fen_zi += item[0] * item[1]
        fen_wu_zuo += math.pow(item[0], 2)
        fen_wu_you += math.pow(item[1], 2)
    return fen_zi / (math.sqrt(fen_wu_zuo) * math.sqrt(fen_wu_you))

def getgoods(users:dict):
    goods = []
    for i in users.items():
        for ii in i[1].keys():
            if ii not in goods:
                goods.append(ii)
    return goods

xiangs_si_du={}
goods=getgoods(users3)
for x in range(len(goods)-1):
    for y in range(x+1,len(goods)):
        key=str(goods[x])+'_'+ str(goods[y])
        xiangs_si_du[key]=calcxiangsidu(str(goods[x]),str(goods[y]),users3)

pass
