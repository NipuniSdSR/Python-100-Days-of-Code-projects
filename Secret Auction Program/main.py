from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo



Bid_list={}
Users=True

def bid_winner(Bid_list):
  max=-1
  max_name=''

  for key in Bid_list:
    if Bid_list[key]>max:
      max_name=key
      max=Bid_list[key]

  print(f"The winner is {max_name} with bid of ${max}")

while Users:
  print(logo)
  Name=input("What is your name?: ")
  Bid=input("What's your bid?: $")
  bidders=input("Are there any other bidders? Type 'yes' or 'no'").lower()
  
  Bid_list[Name]= int(Bid)

  clear()
  if bidders == 'no':
    Users=False
    bid_winner(Bid_list)

  
