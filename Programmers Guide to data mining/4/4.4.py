music = {"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
         "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1, "rap": 1},
         "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4, "backup vocals": 1, "rap": 1},
         "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5, "rap": 1},
         "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5, "backup vocals": 1, "rap": 1},
         "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar":4, "backup vocals": 5, "rap": 1},
         "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2, "backup vocals": 2, "rap": 4},
         "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2, "rap": 1}}

users ={"Angeelica": {"Dr Dog/Fate": "L",
         "Phoenix/Lisztomania": "L",
         "Heartless Bastards/Out at Sea": "D",
         "Todd Snider/Don't Tempt Me": "D",
         "The Black Keys/Magic Potion": "D",
         "Glee Cast/Jessie's Girl": "L",
         "La Roux/Bulletproof": "D",
         "Mike Posner": "D",
         "Black Eyed Peas/Rock That Body": "D",
         "Lady Gaga/Alejandro": "L"},
        "Bill": {"Dr Dog/Fate": "L",
         "Phoenix/Lisztomania": "L",
         "Heartless Bastards/Out at Sea": "L",
         "Todd Snider/Don't Tempt Me": "D",
         "The Black Keys/Magic Potion": "L",
         "Glee Cast/Jessie's Girl": "D",
         "La Roux/Bulletproof": "D",
         "Mike Posner": "D",
         "Black Eyed Peas/Rock That Body": "D",
         "Lady Gaga/Alejandro": "D"}
        }
unKnowUser= {"Angeelica":{"thissong": {"piano": 1, "vocals": 5, "beat": 2.5, "blues": 1, "guitar": 1, "backup vocals": 5, "rap": 1}}}


def manhadunDistance(vector_base,vector1):
    return sum(map( lambda x1,x2:abs(x1-x2),vector_base,vector1))

def calcDistance(items,itemName,itemVector):
    '''
    找到最距离最新的
    :param itemName: 需要查找的名字
    :param itemVector: 需要查找对象的评分数组
    :param items: 原有的评分数组
    :return:
    '''
    distance_list = {}
    for key, value in items.items():
        if (key != itemName):
            distance_list[key] = manhadunDistance(value, itemVector)
    return sorted(distance_list.items(),key=lambda x:x[1])

def classify(items,itemName,itemVector):
    distance = calcDistance(items, itemName, itemVector)
    for key, value in dict(users['Angeelica']).items():
        if distance[0][0] == key:
            return value
    else:
        return 'UNKNOW'


base_dict={}
for key,value in music.items():
    sub_item=dict(value)
    base_dict[key]=list(sub_item.values())

toCompare=[1,5,2.5,1,1,5,1]
toCompare_item_name='thissong'

result=classify(base_dict,toCompare_item_name,toCompare)
pass
