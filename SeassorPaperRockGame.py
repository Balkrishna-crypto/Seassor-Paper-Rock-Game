import random
randNo= random.randint(1,3)
player =input("Enter Seassor 's' or Paper 'p' or Rock 'r' :")
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='r'
print(f"your input for Seassor 's' or Paper 'p' or Rock 'r'     is   :{player}")
print(f"Computer input for Seassor 's' or Paper 'p' or Rock 'r' is   :{comp} ")
def gameWin(player,comp):
    if comp==player:
        return None
    elif comp=='s':
        if player=='p':
            return False
        else:
            return True
    elif comp=='p':
        if player=='r':
            return False
        else:
            return True
    elif comp=='r':
        if player=='s':
            return False
        else :
            return True

a=gameWin(player,comp)
if a==None:
    print("Game is tie!")
elif a:
    print("You Won!")
else:
    print("You Lose!")
        