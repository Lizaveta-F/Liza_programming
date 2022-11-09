from art import logo,vs
from game_data import data
import random
from replit import clear


def format_data(account):
  """Takes athe account data and returns it in printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return(f"{account_name} a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
  """Takes the user's guess and follower's count on A and B and returns if heshe got it right"""
  if a_followers>b_followers:
    return guess == "a"
  else:
    return guess == "b"
    
    
print(logo)
score=0
game_continue = True
account_b = random.choice(data)

while game_continue:
  account_a = account_b
  account_b = random.choice(data)
   
  while account_a == account_b:
    account_b = random.choice(data)
  
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  guess= input("Who has more followers 'A' or 'B'. Type 'A' or 'B': " ).lower()
  
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  clear()
  print(logo)
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  if is_correct:
    score+=1
    print(f"That's right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong.. Your final score: {score}.")
    game_continue = False