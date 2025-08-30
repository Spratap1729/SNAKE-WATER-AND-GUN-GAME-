'''
1 for snake
-1 for water
0 for gun
'''


import random

# Randomly select one value from the list [1, 0, -1]
computer = random.choice([1, 0, -1])


your_choice = input("Enter you choice:")
Dict_choice = {"snake" :1,"water":-1,"gun":0}
reverseDict_choice = {1:"snake",-1:"water",0:"gun"}


you = Dict_choice[your_choice]
print(f"You choose {reverseDict_choice[you]} \n computer choose {reverseDict_choice[computer]}")


if(computer == -1 and you == 1): # (computer - you) = -2
        print("you win !!")
        
elif(computer == -1 and you == 0): # (computer - you) = -1
        print("You loose !!") 

elif(computer == 1 and you == -1): #(computer - you) = 2
        print("You loose !!")

elif(computer == 1 and you == 0): # (computer - you) = 1
        print("You win !!")
elif(computer == 0 and you == -1): #(computer - you) = 1
        print("You win !!")
elif(computer == 0 and you == 1): # (computer - you) = -1 
        print("You loose !!")
else:
    print("It's draw!!")


'''
Advance program:

if(computer == you):
    print("Draw")

else:
    if((computer - you) == -2 or (computer - you) == 1):
        print("You won")
        
    else:
        print("You loose")
    

'''