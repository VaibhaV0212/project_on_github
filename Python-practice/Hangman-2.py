import random
from typing import Tuple

word_list = ['vbv','nid','laal']
choosen_word = random.choice(word_list)
print('choosen_word=>',choosen_word)
display = []
for i in range(len(choosen_word)):
    display += '_'
# print('display=>', display)


end_of_game = False
lives = 3
while not end_of_game:
    guess = input('Guess a letter:- ' ).lower()
    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter == guess:
            display[i] = letter 

    if guess not in choosen_word:            
        lives-=1
        print('lives=>', lives)
        if lives == 0:
            print('You Loose!!')
            end_of_game = True
            
    print('display=>', display) 

    if '_' not in display:
        end_of_game = True       
        print('You Win!!!!')
    
