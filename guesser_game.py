import random


capitals = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna', 'Belgium': 'Brussels',
            'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen', 'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'}


def get_next_country():
    key_ = random.randint(0, len(capitals.keys()) - 1)
    return tuple(capitals.keys())[key_]


def guess_the_capital():
    lives, score, opend_letters = 3, 0, 0

    country = get_next_country()

    while lives > 0:
        input_message = f'Now you unlocked {capitals[country][0:opend_letters]}\n' if opend_letters > 0 else ""
        input_message += f'Guess the capital of {country}: '

        user_answer = input(input_message)

        if user_answer == 'Exit':
            break

        # check answer
        if capitals[country] == user_answer:
            opend_letters = 0
            score += 1
            country = get_next_country()
            print(f'You are right! Your score is {score}\n')
        else:
            lives -= 1
            opend_letters += 1
            print(f'You have {lives} lives left\n')

    if lives > 0:
        print(f'\nCongrats!!! You still have some extra lifes. \nBut you decide to finish, so your final score is {score}')
    else:
        print(f'Game is over. You are looser\nYour final score is just {score}')


guess_the_capital()