import random

def start():
    my_points = []
    computer_points = []
    def comparisons():
        if len(my_points) == 2:
            print('You win! game end!')
            my_points.clear()
            computer_points.clear()
        elif len(computer_points) == 2:
            print('Computer win! game end, try again!')
            my_points.clear()
            computer_points.clear()
            comparisons()
        computer_choice = random.choice(['scissors','rock','paper'])
        my_choice = input('My choice: ')
        #HELP
        if my_choice == '-help':
            print('Game root:\n1. The game starts with your choice: rock, paper or scissors(nothing more).\n2. The game ends when one of the players reaches 10 points')
        #DRAW
        elif my_choice == 'scissors' and computer_choice == 'scissors':
            print(f'\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'rock' and computer_choice == 'rock':
            print(f'\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'paper' and computer_choice == 'paper':
            print(f'\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')

        #I WIN
        elif my_choice == 'scissors' and computer_choice == 'paper':
            my_points.append(1)
            print(f'\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'rock' and computer_choice == 'scissors':
            my_points.append(1)
            print(f'\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'paper' and computer_choice == 'rock':
            my_points.append(1)
            print(f'\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')

        #COMPUTER WIN
        elif my_choice == 'paper' and computer_choice == 'scissors':
            computer_points.append(1)
            print(f'\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'scissors' and computer_choice == 'rock':
            computer_points.append(1)
            print(f'\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'rock' and computer_choice == 'paper':
            computer_points.append(1)
            print(f'\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        else:
            print("Wrong command \nWrite -help, for view more commands")
            comparisons()
        comparisons()
    comparisons()
start()