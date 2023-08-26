from art import logo
from art import vs
import random 
from game_data import data
from replit import clear

random_A = random.randint(0,49)

def returnhehe(random_A):
  name = data[random_A]['name']
  description = data[random_A]['description']
  country = data[random_A]['country']
  return (f"Compare A: {name}, {description}, {country}")

def compare(A_score, B_score):
  if A_score > B_score :
    return "A"
  elif A_score < B_score:
    return "B"

print(logo)
random_B = random.randint(0,49)
A_score = data[random_A]['follower_count']
B_score = data[random_B]['follower_count']

user_score = 0
game_over = False


while not game_over:
  top_char = random_B
  random_B = random.randint(0,49)
  print(f" Compare A: {returnhehe(top_char)}")
  print(vs)
  print(f"Compare B: {returnhehe(random_B)}")
  chose = input("Choose 'A' or 'B' :")
  clear()
  print(logo)
  if chose == compare(A_score, B_score):
    user_score +=1
    print(f"You got it correctly!. You have {user_score} points")
  else:
    clear()
    print(logo)
    print(f"YOU ARE WRONG! Your final score is {user_score}")
    game_over = False
    
    
  
  





  



     
