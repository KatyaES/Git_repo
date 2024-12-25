import random

def computer_step(computer_options):
    result = random.choice(computer_options)
    return result
computer_choice = computer_step(['scissors','rock','paper'])

def my_step(result):
    return result
my_choice = my_step(input('My choisce: '))

def comparisons():
    my_points = 0
    computer_points = 0
    """Draw"""
    if my_choice == 'scissors' and computer_choice == 'scissors':
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{my_points}      {computer_points}')
    elif my_choice == 'rock' and computer_choice == 'rock':
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{my_points}      {computer_points}')
    elif my_choice == 'paper' and computer_choice == 'paper':
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{my_points}      {computer_points}')

    """I WIN"""
    if my_choice == 'scissors' and computer_choice == 'paper':
        my_points = my_points + 1
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{my_points}      {computer_points}')
    elif my_choice == 'rock' and computer_choice == 'scissors':
        my_points = my_points + 1
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{my_points}      {computer_points}')
    elif my_choice == 'paper' and computer_choice == 'rock':
        my_points = my_points + 1
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{my_points}      {computer_points}')

    """COMPUTER WIN"""
    if my_choice == 'paper' and computer_choice == 'scissors':
        computer_points = computer_points + 1
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{my_points}      {computer_points}')
    elif my_choice == 'scissors' and computer_choice == 'rock':
        computer_points = computer_points + 1
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{my_points}      {computer_points}')
    elif my_choice == 'rock' and computer_choice == 'paper':
        computer_points = computer_points + 1
        print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{my_points}      {computer_points}')
 
comparisons()
