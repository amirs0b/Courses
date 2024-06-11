import random as rd
from art import logo,vs
from game_data import data

DATA_COUNT = len(data)

def pickName():
    select = []
    for i in range(2):
        a = rd.randint(0,DATA_COUNT-1)
        if a not in select:
            select.append(a)
        else:
            pickName()
    
    name_A = data[select[0]]
    name_B = data[select[1]] 

    print(f"Compare A: {name_A["name"]}, a {name_A["description"]}, from {name_A['country']}")
    print(vs)
    print(f"Against B: {name_B["name"]}, a {name_B["description"]}, from {name_B['country']}")
    
    return [name_A["follower_count"], name_B['follower_count']]



def play_game():
    print(logo)
    score = 0
    while True:
        cards = pickName()
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_choice not in ["a", "b"]:
            print("Invalid input. Please type 'A' or 'B'.")
            continue

        if (user_choice == "a" and cards[0] > cards[1]) or (user_choice == "b" and cards[0] < cards[1]):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            break

play_game()




"""
You're right! Current score: 1.
Compare A: Victoria's Secret, a Lingerie brand, from United States.
Sorry, that's wrong. Final score: 1
Compare A: Kim Kardashian, a Reality TV personality and businesswoman, from United States.
Against B: Camila Cabello, a Musician, from Cuba.
Who has more followers? Type 'A' or 'B':

"""