import random

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
bet_number = None
bank_account = 1000

bet_amount = int(input("Place bet amount please"))
bet_color = input("What color do you want to bet on?")
bet_number = int(input("What numbers do you want to bet on?"))
print("-----------------------------------")
print("-----------------------------------")

roll_ballnumber = random.randint(0, 37)
print("Landing number is: ")
print(roll_ballnumber)

if bet_number == roll_ballnumber:
  print("You Win")
else:
  print("You Lose")
print("-----------------------------------")
print("Landing color is: ")

if roll_ballnumber in red:
  print("Red Wins")
elif roll_ballnumber in black:
  print("Black Wins")
else:
  print("Green Wins")
