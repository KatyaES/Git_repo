import random

#features
#i want to add new feature
#New commit
#fourth line was added
#it is a 5 line

def start():
    my_points = []
    computer_points = []
    def comparisons():
        computer_choice = random.choice(['scissors','rock','paper'])
        my_choice = input('My choice: ')
        """Draw"""
        if my_choice == 'scissors' and computer_choice == 'scissors':
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'rock' and computer_choice == 'rock':
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'paper' and computer_choice == 'paper':
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Draw\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')

        #I WIN
        elif my_choice == 'scissors' and computer_choice == 'paper':
            my_points.append(1)
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'rock' and computer_choice == 'scissors':
            my_points.append(1)
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'paper' and computer_choice == 'rock':
            my_points.append(1)
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: You win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')

        #COMPUTER WIN
        elif my_choice == 'paper' and computer_choice == 'scissors':
            computer_points.append(1)
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'scissors' and computer_choice == 'rock':
            computer_points.append(1)
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        elif my_choice == 'rock' and computer_choice == 'paper':
            computer_points.append(1)
            print(f'You: {my_choice}\nComputer: {computer_choice}\nResult: Computer win!\nME  COMPUTER\n{len(my_points)}      {len(computer_points)}')
        comparisons()
    comparisons()
start()
