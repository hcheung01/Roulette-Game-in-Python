import random

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
bet_number = None
bank_account = 1000

print("-----------------------------------")
bet_amount = int(input("Place bet amount for a number please "))
bet_amount2 = int(input("Place bet amount for a color please "))
bet_color = str(input("What color do you want to bet on? "))
bet_number = int(input("What numbers do you want to bet on? "))
bet_difference = bank_account - bet_amount - bet_amount2
bet_winner = (bet_amount * 2) + (bet_amount2 * 2) + bet_difference

print("-----------------------------------")
print("-----------------------------------")
print("Current Balance         $" + repr(bank_account))
print("You total bet amount is  " + "-$" + repr(bet_amount + bet_amount2))
print("Remaining balancing is " + "  $" + repr(bet_difference))
print("-----------------------------------")
print("-----------------------------------")


roll_ballnumber = random.randint(0, 37)
if roll_ballnumber == 37:
  roll_ballnumber = int("00")
  print("Winning # is: " + repr(roll_ballnumber))
else:
  print("Winning # is: " + repr(roll_ballnumber))

if bet_number == roll_ballnumber:
  print("You Win " + "$" + repr(bet_amount))
else:
  print("You Lose " + "$" + repr(bet_amount))
print("-----------------------------------")


if roll_ballnumber in red:
  print("Landing color is: Red")
elif roll_ballnumber in black:
  print("Landing color is: Black")
else:
  print("Landing color is: Green")

if bet_color == red:
  print("You Win " + repr(bet_amount2))
elif bet_color == black:
  print("You Win " + repr(bet_amount2))
else:
  print("You Lose " + repr(bet_amount2))
print("-----------------------------------")

if bet_number == roll_ballnumber:
  print("Your remaining balance $" + repr(bet_winner))
else:
  print("Your remaining balance $" + repr(bet_difference))
