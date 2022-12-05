#Import logo
from art import logo,vs
print(logo)

# choose random data from given information
import random
from game_data import data


def get_data():
  return random.choice(data)

#print details of random data
def print_data(index):
  return f"{index['name']},a {index['description']}, from {index['country']}, "


#compare the guess and answer
def compare(quiz_A,quiz_B,player_choice):
  followers_A=quiz_A['follower_count']
  followers_B=quiz_B['follower_count']
  
  
  # if (followers_A>followers_B and player_choice=='a') or (followers_A<followers_B and player_choice=='b'):
  #   return 1
  # else:
  #   return 0
  if followers_A>followers_B:
    return player_choice=='a'
  else:
    return player_choice=='b'



from replit import clear

def game_higher_lower():

  score=0
  quiz_B=get_data()
  play=True



  while play:
    
    quiz_A=quiz_B
    
    while quiz_B == quiz_A:
      quiz_B=get_data()

    print(f"Compare A: {print_data(quiz_A)}")
    print(vs)
    print(f"Against B: {print_data(quiz_B)}")
    player_choice=input("Who has more followers? Type 'A' or 'B': ").lower()
  
    result=compare(quiz_A,quiz_B,player_choice)
    clear()
    print(logo)
    
    if result == True:
      score+=1
      print(f"You're right! Your current socore: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return

    


    
game_higher_lower()  