import random
count=0
while(count<=100):
    a=input("enter 'r' to roll a dice=")
    if (a=='r'):
        r=random.randint(1,6)
        count=count+r
        print("dice value=")
        print(r)
        print("count value=")
        print(count)
    if (count==8):
        count=37
        print("you climed the ladder")
    elif(count==11):
        count=2
        print("your fired")
    elif(count==13):
        count=34
        print("you climed the ladder")
    elif(count==25):
        count=4
        print("you are bitten")
    elif(count==38):
        count=9
        print("you are bitten")
    elif(count==40):
        count=68
        print("you climed the ladder")
    elif(count==52):
        count=81
        print("you are near")
    elif(count==65):
        count=46
        print("loser")
    elif(count==76):
        count=97
        print("almost near")
    elif(count==89):
        count=70
        print("boo")
    elif(count==93):
              count=64
              print("ha ha ha")
    else:
        if count==100:
           print("you rule")
    

