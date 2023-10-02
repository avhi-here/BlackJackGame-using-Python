import random
import os
#from art import logo
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(l):
  if sum(l) == 21 and len(l) == 2:
    return 0
  if 11 in l and sum(l)>21:
    l.remove(11)
    l.append(1)
  return sum(l)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return '''
      _                    
     | |                   
   __| |_ __ __ ___      __
  / _` | '__/ _` \ \ /\ / /
 | (_| | | | (_| |\ V  V / 
  \__,_|_|  \__,_| \_/\_/  
                           
                           
'''
  elif computer_score == 0:
    return '''  
  _           _   
 | |         | |  
 | | ___  ___| |_ 
 | |/ _ \/ __| __|
 | | (_) \__ \ |_ 
 |_|\___/|___/\__|
                  
 opponent has a BlackJack :('''
  elif user_score == 0:
    return '''            
 __      _____  _ __  
 \ \ /\ / / _ \| '_ \ 
  \ V  V / (_) | | | |
   \_/\_/ \___/|_| |_|
                      
  with a BlackJack :)'''
  elif user_score > 21:
    return '''
    You went over!
  _           _   
 | |         | |  
 | | ___  ___| |_ 
 | |/ _ \/ __| __|
 | | (_) \__ \ |_ 
 |_|\___/|___/\__|
                  
                  '''
  elif computer_score > 21:
    return '''
    Opponent went over!
 __      _____  _ __  
 \ \ /\ / / _ \| '_ \ 
  \ V  V / (_) | | | |
   \_/\_/ \___/|_| |_|
                      
    '''
  elif user_score > computer_score:
    return '''                      
                      
 __      _____  _ __  
 \ \ /\ / / _ \| '_ \ 
  \ V  V / (_) | | | |
   \_/\_/ \___/|_| |_|
                      
                      '''
  else:
    return  '''
  _           _   
 | |         | |  
 | | ___  ___| |_ 
 | |/ _ \/ __| __|
 | | (_) \__ \ |_ 
 |_|\___/|___/\__|
                  
                  '''

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over=False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    
    print(f"\tYour cards: {user_cards}, current score = {sum(user_cards)}")
    print(f"\tComputers first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over=True
    else:
      choice=input("Type 'y' to get another card, else 'n' to pass: ")
      if choice == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand {user_cards}, Final Score: {user_score}")
  print(f"Opponents final hand {computer_cards}, Final Score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' for YES, else 'n' for NO:") == "y":
  os.system('cls||clear')
  play_game()

    