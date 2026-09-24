'''
1 for snake
-1 for water
0 for gun
'''
import random

com = random.choice([-1,0,1])
youstr = input("Enter your opyion = ")
youdict= {"s": 1, "w": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0:"Gun"}
you = youdict[youstr]

print(f"You choose {reversedict[you]}\nComputer choose {reversedict[com]}")

if(com == you):
    print("Its a Drae !")

else:
    if(com == -1 and you == 1):
        print("You win!")
    elif(com == -1 and you == 0):
        print("You lose!")


    elif(com == 1 and you == -1):
        print("You lose!")
    elif(com == 1 and you == 0):
        print("You win!")


    elif(com == 0 and you == -1):
        print("You win!")
    elif(com == 0 and you == 1):
        print("You lose!")

    else:
        print("Something went wrong!")


