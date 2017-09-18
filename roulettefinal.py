import random

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
bet_number = None
bank_account = 1000

bet_amount = int(input("Place bet amount please"))
bet_color = input("What color do you want to bet on?")
bet_number = int(input("What numbers do you want to bet on?"))

def take_bet(color, number, amount):
  bet_color = color
  bet_number = number
  bet_amount = amount

def roll_ball():
  roll_ballnumber = random.randint(0, 37)
  print("Winning number is:")
  return roll_ballnumber
print(roll_ball())

def check_results():
  if bet_number in red:
    print("red")
  elif bet_number in black:
    print("black")
  elif bet_number in green:
    print("green")

  if roll_ballnumber in red:
    print("Red")
  elif roll_ballnumber in black:
    print("Black")
  else:
    print("Green")
