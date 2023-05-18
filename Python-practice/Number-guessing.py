import random
from tabnanny import check
# import numpy as np

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 3

def set_difficulty():
    ''' Function to set the diffucluty as easy or hard!'''
    level = input("Choose the type of level? 'Easy' or 'Hard': ").lower()

    if level == 'easy':
        return EASY_LEVEL_TURNS
            
    elif level == 'hard':
        return HARD_LEVEL_TURNS
        

def check_ans(user_guess, num, turns):
    ''' Function to check the answer!'''
    if user_guess > num:
        print('Too High..')
        return turns - 1
    elif user_guess < num:
        print('Too Low..')
        return turns - 1
    else:
        print(f'You got the ans {num}')


# --------------------------------------------------------------------------
def game():
    print("""
        Welcome to Number guessing game!
        I am thinking of a no. between 1-100
        """)

    # num = random.choice(np.arange(1,100))
    num = random.randint(1,100)
    print('Num==>', num)

    turns = set_difficulty()

    guess = 0
    while guess != num:
        print(f'You have {turns} attempts remaining!')
        user_guess = int(input('Make a guess: '))

        turns = check_ans(user_guess, num, turns) 
        if turns == 0:
            print('Sorry turns are over..')
            return 
        elif user_guess != num:
            print('Guess agaian..')
        


game()