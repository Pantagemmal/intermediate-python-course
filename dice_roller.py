import random


def main():
  dice_rolls = 2
  dice_sum = 0
  for i in (0, dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_sum += roll
  
  print(f'You have rolled a {dice_sum} in total')


if __name__== "__main__":
  main()