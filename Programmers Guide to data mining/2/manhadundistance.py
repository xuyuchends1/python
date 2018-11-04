import math
import copy
from functools import reduce
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manHaDunDistance(user1: dict,user2:dict):
    key1=set(user1.keys())
    key2=set(user2.keys())
    both_have_key=key1.intersection(key2)

    distance=0
    for both_key in both_have_key:
        distance+=abs(user1[both_key]- user2[both_key])
    return distance


def computeNeighbor(user_key,user_values,users:dict):
    users_new=copy.deepcopy(users)
    if user_key in users_new:
         del users_new[user_key]

    x_user=dict({user_key:user_values})
    neighbor=dict()
    for user in users_new:
        distance=manHaDunDistance(user_values,users_new[user])
        neighbor[user]=distance
    neighbor=sorted(neighbor.items(),key=lambda item:item[1])
    return neighbor

def piErXun(array_x,array_y):
    xy=0
    x_sum=0
    y_sum=0
    x_pow_sum=0
    y_pow_sum=0
    n=len(array_x)
    for index,value in enumerate(array_x):
       xy+=array_x[index]*array_y[index]
       x_sum+=array_x[index]
       y_sum+=array_y[index]
       x_pow_sum+=pow(array_x[index],2)
       y_pow_sum += pow(array_y[index], 2)

    r=(xy-(x_sum*y_sum/n))/ (math.sqrt(x_pow_sum-(pow(x_sum,2)/n))* math.sqrt(y_pow_sum-(pow(y_sum,2)/n)))
    return r

value1= manHaDunDistance(users["Hailey"],users["Veronica"])
value2= manHaDunDistance(users["Hailey"],users["Jordyn"])

key='Hailey'
value={"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0}
computeNeighbor('Hailey',value,users)

array_x=[4.75,4.5,5,4.25,4]
array_y=[4,3,5,2,1]

r=piErXun(array_x,array_y)
pass
