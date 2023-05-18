import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_cards():
    card = random.choice(cards)
    return card

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "<<Draw>>"
    elif user_score > comp_score:
        return 'User wins'
    elif user_score == 0:
        return 'User Wins!!!'
    elif comp_score == 0:
        return 'Lose, opponent as Blackjack!'
    elif user_score > 21:
        return 'You went over chacha!! Computer Wins!!'
    elif comp_score > 21:
        return 'You Lost Bhaijaan!! User Win!!'
    else:
        return 'Computer Wins...'
    


def calculate_score(a):
    if sum(a) == 21 and len(a) == 2:
        return 0
    
    if 11 in a and sum(a) > 21:
        a.remove(11)
        a.append(1) 
    return sum(a)

def game():
    user = []
    comp = []
    end_of_game = False

    for _ in range(2):
        user.append(deal_cards())
        comp.append(deal_cards())

    while end_of_game != True:

        user_score = calculate_score(user)
        comp_score = calculate_score(comp)

        print(f'user cards are {user} & score {user_score} and computer first card is {comp[0]}')

        if user_score == 0 or comp_score == 0 or user_score > 21:
            end_of_game = True
        else:
            user_should_deal = input("Type 'y' to play?").lower()
            if user_should_deal == 'y':
                user.append(deal_cards())
            else:
                end_of_game = True


    while comp_score !=0 and comp_score < 17:
        comp.append(deal_cards())
        comp_score = calculate_score(comp)
    print(f'  Your final hand {user} and score is {user_score}')
    print(f'  Computer final hand {comp} and score is {comp_score}')

    print(compare(user_score, comp_score))

while input('Want to play type yes?? ').lower() == 'yes':
    game()
