from logo import logo
from replit import clear
import random


print(logo)


def random_card():
  """Generates random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Takes a list of cards and returns the sum of all cards in the list. Checks if the sum is equal or over 21."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(user, computer):
  """Compares the scores of user and computer"""
  if user == computer:
    return "Draw"
  elif user == 21 and computer == 21:
    return "Lose - Lose"
  elif computer == 0:
    return "Computer wins BLACKJACK"
  elif user == 0:
    return "You won! BLACKJACK"
  elif user > 21:
    return "You lose"
  elif computer > 21:
    return "Computer loses"
  elif user > computer:
    return "You won!"
  else:
    return "Computer wins"



def game():
  user_cards = []
  computer_cards = []
  game_over = False
  
  for i in range(2):
    user_cards.append(random_card())
    computer_cards.append(random_card())
  
  
   
  while not game_over:  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      should_continue = input("Type y to draw another card, type n to pass: ")
      if should_continue == "y":
        user_cards.append(random_card())
      else:
        game_over = True
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(random_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  game()