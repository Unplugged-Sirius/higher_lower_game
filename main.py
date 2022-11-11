import random
from game_data import *
from logs import *

a = random.choice(data)
b = random.choice(data)
print (logo)
s = True
score = 0
def check (a ,b):
    if(a['follower_count'] > b['follower_count'] ):
        return "a"
    else:
        return "b"
while (s == True):
    print(f"which has higher folowers A) {a['name']} a {a['description']} from {a['country']}")
    print(vs)
    print(f"  B) {b['name']} a {b['description']} from {b['country']}")
    des = input("enter a or b ")
    ans = check(a , b)
    if(des == ans):
        score+=1
        a = b
        b = random.choice(data)
    else:
        print("ops you loose")
        print(f"your score is {score}")
        s = False