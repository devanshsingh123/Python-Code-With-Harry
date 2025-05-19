import random

# Computer choosing at Random 
print('''
WELCOME TO THE SNAKE , WATER , GUN GAME 
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players 
use hand gestures to represent a snake, water, or a gun. 
The gun beats the snake, the water beats the gun, and the snake beats the water.      
''')

def snake_gun_water(contestant_val,computer_val):
    if(computer_val == contestant_val):
        c_val = input(f"CHOSE SAME VALUE . INPUT YOUR CHOICE FROM SNAKE : S , WATER : W , GUN : G  -> ")
        com_val = random.choice('SGW')
        return snake_gun_water(c_val,com_val)
    elif((contestant_val == 'S' and computer_val == 'W' ) or (contestant_val == 'G' and computer_val == 'S' ) or (contestant_val == 'W' and computer_val == 'G' )):
        return "YOU WON !"
    else:
        return "YOU LOST !"

contestant_val = input(f"INPUT YOUR CHOICE FROM SNAKE : S , WATER : W , GUN : G  -> ")

computer_val = random.choice('SGW')

Result = snake_gun_water(contestant_val,computer_val)
print(Result)



    





