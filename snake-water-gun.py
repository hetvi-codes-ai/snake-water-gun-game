import random
'''
1 = snake
-1 = water
0 = gun   game!
'''
com = random.choice([-1,0,1])
str=input("enter your choice:")
dictt={"s":1,"w":-1,"g":0}
rdict={1:"snake",-1:"water",0:"gun"}
you=dictt[str]
print(f"you chose {rdict[you]}\n computer chose {rdict[com]}")
if(com==you):
    print("its a draw")
else:
    if(com==-1 and you==1):
        print("you win")
    elif(com==-1 and you==0):
        print("you lose")
    elif(com==1 and you==-1):
        print("you lose")
    elif(com==1 and you==0):
        print("you win")
    elif(com==0 and you==-1):
        print("you win")
    elif(com==0 and you==1):
        print("you lose")
    else:
        print("something wrong")
