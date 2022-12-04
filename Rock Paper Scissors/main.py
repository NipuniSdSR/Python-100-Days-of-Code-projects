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
hand=[rock, paper, scissors]
player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer= random.randint(0,2)

c="You lost"
p=" You win"
d="Draw"
win="0"

if player == 0:
  if computer == 0:
    win=d
  elif computer == 1:
    win =c
  else:
    win = p
elif player == 1:
  if computer == 0:
    win=p
  elif computer == 1:
    win =d
  else:
    win = c  
elif player == 2:
  if computer == 0:
    win=c
  elif computer == 1:
    win =p
  else:
    win = d
else:
  win="give a valid number"

print("you chose :\n"+ hand[player]+"\n")
print("computer chose :\n"+ hand[computer]+"\n")
print(win)