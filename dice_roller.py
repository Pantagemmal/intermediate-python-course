import random


def main():
  x = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides the dice have? '))
  dice_sum = 0

  for i in (0,x):
    
    roll = random.randint(1,dice_size)

    if roll == dice_size:
      print(f'You rolled a {roll}. Caralho rapaz!')
    elif roll == 1:
      print(f'You rolled a {roll}. Se fodeu!')
    else:
      print(f'You rolled a {roll}')
    dice_sum += roll
  
  print(f'You have rolled a {dice_sum} in total')


if __name__== "__main__":
  main()