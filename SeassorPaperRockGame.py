import random

CHOICE='spr'

#defining the funtion to chose s p r with the help of random function
def get_computer_choice():
    
    Comp_option = random.randint(0, 2)
    Comp_option = CHOICE[Comp_option]
    return Comp_option


Comp_option=get_computer_choice()
player =input("Enter Seassor 's' or Paper 'p' or Rock 'r' :")
print(f"Your input for Seassor 's' or Paper 'p' or Rock 'r'     is   :{player}")
print(f"Computer input for Seassor 's' or Paper 'p' or Rock 'r' is   :{Comp_option} ")


player=player.lower()
def gameWin(player,Comp_option):
    if Comp_option==player:
        return None
    elif Comp_option=='s':
        if player=='p':
            return False
        else:
            return True
    elif Comp_option=='p':
        if player=='r':
            return False
        else:
            return True
    elif Comp_option=='r':
        if player=='s':
            return False
        else :
            return True

a=gameWin(player,Comp_option)
if a==None:
    print("Game is tie!")
elif a:
    print("You Won!")
else:
    print("You Lose!")
        