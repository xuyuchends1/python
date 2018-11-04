import math
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


def oushiDistance(vector1,vector_base):
    return math.sqrt(sum(map(lambda x1,x2:pow(x1-x2,2),vector1,vector_base)))

def manhadunDistance(vector1,vector_base):
    return sum(map(lambda x1,x2:abs(x1-x2),vector1,vector_base))

def getDistance(music1,music_base, method="oushi"):
    music1_dict= sorted(music[music1].items(),key=lambda x: x[0]);
    music_base_dict = sorted(music[music_base].items(), key=lambda x: x[0]);
    music1_list=[ x[1]  for x in music1_dict]
    music_base_list = [x[1] for x in music_base_dict]
    if ('oushi'):
        return oushiDistance(music1_list, music_base_list)
    elif ('manhadun'):
        return manhadunDistance(music1_list,music_base_list)
    else:
        raise Exception('error')

def getFamilarOne(music_name, method):
    distance_list = {}
    for key, music_value in music.items():
        if (key != music_name):
            distance_list[key] = getDistance(key, music_name,method)
    return sorted(distance_list.items(),key=lambda x:x[1] )[0]


distance1 = getDistance("Dr Dog/Fate","Glee Cast/Jessie's Girl")
distance2 = getDistance("Lady Gaga/Alejandro","Glee Cast/Jessie's Girl")

music_name1=getFamilarOne("The Black Keys/Magic Potion","manhadun")
pass