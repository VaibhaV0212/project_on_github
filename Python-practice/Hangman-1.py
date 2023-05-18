import random

# 1: randomly choose a word and assign it to a variable

word_list = ['vbv','nid','laal']
choosen_word = random.choice(word_list)

# 2: ask the user to guess a letter and assign it to a variable and make it in lowercase
# guess = input('Guess a letter:- ' ).lower()

# 3: check the 'guess' is present in any of the letters?
# for i in choosen_word:
#     if guess == i:
#         print('found') 
#     else: print('not found')
    

# 4: create a new list 'display' and replace with blanks for all the letters in choosen_word
# display = [i.replace(i, '_') for i in choosen_word]
display = []
for i in range(len(choosen_word)):
    display += '_'

print('display=>', display)
guess = input('Guess a letter:- ' ).lower()

# 5: Unhide the letters if guess is Right

for i in range(len(choosen_word)):
    letter = choosen_word[i]
    if letter == guess:
        display[i] = letter 
print('display=>', display)        
