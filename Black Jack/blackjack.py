import art
import random
from replit import clear


def calculate_score(cards):
  if sum(cards)==21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has a Black Jack"
  elif user_score == 0:
    return "You win with a Black Jack!"
  elif user_score > 21:
    return "You lose"
  elif computer_score >21:
    return "You win! Opponent went over"
  elif user_score>computer_score:
    return "You win"
  else:
    "You lose"

  
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def play_game():
  print(art.logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"You cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card and 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  while computer_score!=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final cards are {user_cards} and final score {user_score}")
  print(f"Opponent's final cards are {computer_cards} and final score {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you wanna play the game of Black Jack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

  
        
    