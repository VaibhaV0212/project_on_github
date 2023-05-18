from data import data
import random


def format(accounts):
    account_name  = accounts['name']
    account_desc = accounts['description']
    account_country = accounts['country']
    return f'{account_name}, {account_desc}, {account_country}'

def check(user, a_follower, b_follower):
    if a_follower > b_follower:
        return user == "a"
    else:
        return user == "b"

end = False
score = 0
while end != True:

    A = random.choice(data)
    B = random.choice(data)
    if A == B:
        B = random.choice(data) 

    print(f'Compare A : {format(A)}\n')
    print(f'Compare B : {format(B)}')

    user = input('Enter your guess "A" or "B"? ').lower()

    a_follower = A['follower_count']
    b_follower = B['follower_count']

    
    is_correct = check(user, a_follower, b_follower)

    if is_correct:
        score +=1
        print(f'You are correct and score is {score}')
        
    else: 
        print(f'You are wrong and score is {score}')
        end = True




#     print(f'User is correct and count is {a_follwer}')
#     score += 1
# elif b_follwer > a_follwer:
#     print(f'Wrong ans & score is {score}')