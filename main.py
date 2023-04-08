import random

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

random_ = [rock, paper, scissors]
random_choice = random.choice(random_)
Iswin = False
qst = input("What would you like to choose? Rock, Paper or Scissors. ").lower()

if qst == 'rock':
	print("\nYou chose:")
	print(rock)
	print(f"\nComputer chose:{random_choice}")
	if random_choice == rock:
		print('Tie!')
	elif random_choice == scissors:
		print("You win! Rock smashes Scissors!!!")
	else:
		print("You loose! Paper beats Scissors!")
elif qst == 'paper':
	print("\nYou chose:")
	print(paper)
	print(f"\nComputer chose: {random_choice}")
	if random_choice == rock:
		print("You win! Paper beats Rock!!!")
	elif random_choice == paper:
		print("Tie!")
	else:
		print("You loose!!")
elif qst == 'scissors':
	print("\nYou chose:")
	print(scissors)
	print(f"\nComputer chose: {random_choice}")
	if random_choice == paper:
		print("You win!! Scissors beats Paper")
	elif random_choice == scissors:
		print("Tie!")
	else:
		print("You loose!")
else:
	print("Invalid request")
