rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

list = [rock, paper, scissors]
choices = ['rock', 'paper', 'scissors']
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))

computer_choice =  random.randint(0,2)

print(list[user])

print(f"Computer chose:\n{list[computer_choice]}")

if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
elif user == 0 and computer_choice == 2:
    print("You win!")
elif user == 2 and computer_choice == 0:
    print("You win!")
elif computer_choice > user:
    print("You lose")
elif computer_choice == user:
    print("It's a draw!")
elif computer_choice < user:
    print("You win!")

# if user not in [0, 1, 2]:
#     print("You typed an invalid number, you lose!")
# else:
#     computer_choice = random.randint(0, 2)
#     print(f"Computer chose:\n{choices[computer_choice]}")
#     if user == computer_choice:
#         print("It's a draw!")
#     elif (user - computer_choice) % 3 == 1:
#         print("You win!")
#     else:
#         print("You lose")