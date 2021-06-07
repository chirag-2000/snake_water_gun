def game(you,comp):
    if(you==comp):
        return None
    elif(you=="w" and comp=="g"):
        return True
    elif(you=="g" and comp=="w"):
        return False
    elif(you=="s" and comp=="w"):
        return True
    elif(you=="w" and comp=="s"):
        return False
    elif(you=="g" and comp=="s"):
        return True
    elif(you=="s" and comp=="g"):
        return False


import random
RNO=random.randint(1,3)
if(RNO==1):
    comp="s"
elif(RNO==2):
    comp="w"
else:
    comp="g"

print("\nYOUR TURN")
you=input("Enter (s) for snake, (w) for water ,(g) for gun : ")

result=game(you,comp)
print("COMPUTER CHOSE :",comp,"AND YOU CHOSE: ",you)

if(result==None):
    print("DRAW!!")
elif(result==True):
    print("You WON :) ")
else:
    print("YOU LOST")
