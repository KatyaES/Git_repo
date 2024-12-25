import random

phrases_ru_my = ['Ð¡ Ñ‡ÐµÐ»Ð¾Ð²ÐµÐºÐ¾Ð¼ Ð½Ð¸Ñ‡Ñ‚Ð¾ Ð½Ðµ ÑÑ€Ð°Ð²Ð½Ð¸Ñ‚ÑÑ!', 'Ð¢Ñ‹ Ð½Ð°Ð´ÐµÑÐ»ÑÑ Ð¾Ð±Ñ‹Ð³Ñ€Ð°Ñ‚ÑŒ Ñ‡ÐµÐ»Ð¾Ð²ÐµÐºÐ°?Ð˜Ð½Ñ‚ÐµÑ€ÐµÑÐ½Ñ‹Ð¹ Ñ‚Ñ‹', 'Ð›ÐµÐ¶Ð°Ñ‚ÑŒ, Ð±Ð¾ÑÑ‚ÑŒÑÑ!']
phrases_ru_pc = ['ÐšÑƒÐ´Ð° Ñ‚Ñ‹ Ð»ÐµÐ·ÐµÑˆÑŒ Ð¿Ñ€Ð¾Ñ‚Ð¸Ð² ÐºÐ¾Ð¼Ð¿ÑŒÑŽÑ‚ÐµÑ€Ð°, Ð´ÑÐ±Ð¸Ð»ÑƒÑˆÐºÐ°?', 'Ð¿Ñ„Ñ„ Ð¸Ð·Ð¸', 'Ð½Ñƒ Ñ‡Ñ‚Ð¾, ÐºÑ‚Ð¾ ÑÐ»ÐµÐ´ÑƒÑ‰Ð¸Ð¹?']
phrases_pc_eu = ['PC is the best!', 'Funny', 'Amusing']
phrases_my_eu = ['Eyse', 'More?:)', 'Who next?-_-', 'exe exe exe']
nicknames_pc = ['Invincible', 'DoctorPaper', 'I am Groot']
name_pc = random.choice(nicknames_pc)


def lang():
    print('Select a language(Ð’Ñ‹Ð±ÐµÑ€ÐµÑ‚Ðµ ÑÐ·Ñ‹Ðº): eu, ru')
    language = input('>>> ')
    if language == 'eu' or language == 'ÑƒÐ³':
        print('If you want to stop the program and see medals enter "stop"')
        lis = ['rock', 'paper', 'scissors']
        my_medals = []
        pc_medals = []
        print('Maybe you should get a nickname?')
        name = input('Enter name >>> ')

        def game_with_pc():
            my_answer = input(f'rock, scissors or paper? >>> ')
            print(f'{name}: {my_answer}')
            if my_answer == 'stop':
                my = len(my_medals)
                pc = len(pc_medals)
                print(f'My medals: {my}')
                print(f'{name_pc} medals: {pc}')
                if my_medals > pc_medals:
                    print(random.choice(phrases_my_eu))
                elif my_medals == pc_medals:
                    print('Need revenge')
                else:
                    print(random.choice(phrases_pc_eu))
            elif my_answer == 'rock' or my_answer == 'scissors' or my_answer == 'paper':
                answer_pc = random.choice(lis)
                print(f'{name_pc}: {answer_pc}')
                if answer_pc == 'rock' and my_answer == 'rock':
                    print('Draw')
                elif answer_pc == 'paper' and my_answer == 'paper':
                    print('Draw')
                elif answer_pc == 'scissors' and my_answer == 'scissors':
                    print('Draw')
                    # if me win
                elif my_answer == 'rock' and answer_pc == 'scissors':
                    print('You win')
                    my_medals.append('ðŸ…')
                elif my_answer == 'paper' and answer_pc == 'rock':
                    print('You win')
                    my_medals.append('ðŸ…')
                elif my_answer == 'scissors' and answer_pc == 'paper':
                    print('You win')
                    my_medals.append('ðŸ…')
                    # if PC win
                elif answer_pc == 'rock' and my_answer == 'scissors':
                    print(f'{name_pc} win')
                    pc_medals.append('ðŸ…')
                elif answer_pc == 'paper' and my_answer == 'rock':
                    print(f'{name_pc} win')
                    pc_medals.append('ðŸ…')
                elif answer_pc == 'scissors' and my_answer == 'paper':
                    print(f'{name_pc} win')
                    pc_medals.append('ðŸ…')
                game_with_pc()
            else:
                print('Please, select only the above answers')
                game_with_pc()

        game_with_pc()
    elif language == 'ru' or language == 'ÐºÐ³':
        print('Ð•ÑÐ»Ð¸ Ð²Ñ‹ Ð·Ð°Ñ…Ð¾Ñ‚Ð¸Ñ‚Ðµ Ð¾ÑÑ‚Ð°Ð½Ð¾Ð²Ð¸Ñ‚ÑŒ Ð¿Ñ€Ð¾Ð³Ñ€Ð°Ð¼Ð¼Ñƒ Ð¸ Ð¿Ð¾ÑÐ¼Ð¾Ñ‚Ñ€ÐµÑ‚ÑŒ Ð¾Ñ‡ÐºÐ¸ Ð²Ð²ÐµÐ´Ð¸Ñ‚Ðµ "ÑÑ‚Ð¾Ð¿"')
        lis = ['ÐºÐ°Ð¼ÐµÐ½ÑŒ', 'Ð±ÑƒÐ¼Ð°Ð³Ð°', 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹']
        my_medals = []
        pc_medals = []
        print('ÐœÐ¾Ð¶ÐµÑ‚ Ñ‚ÐµÐ±Ðµ Ð¾Ð±Ð·Ð°Ð²ÐµÑÑ‚Ð¸ÑÑŒ Ð½Ð¸ÐºÐ¾Ð¼?')
        name = (input('Ð’Ð²ÐµÐ´Ð¸ Ð½Ð¸Ðº >>> '))

        def game_with_pc():
            my_answer = input('ÐºÐ°Ð¼ÐµÐ½ÑŒ, Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹ Ð¸Ð»Ð¸ Ð±ÑƒÐ¼Ð°Ð³Ð°? >>> ')
            print(f'{name}: {my_answer}')
            if my_answer == 'ÑÑ‚Ð¾Ð¿':
                my = len(my_medals)
                pc = len(pc_medals)
                print(f'ÐœÐ¾Ð¸ Ð¼ÐµÐ´Ð°Ð»Ð¸: {my}')
                print(f'ÐœÐµÐ´Ð°Ð»Ð¸ {name_pc}: {pc}')
                if my_medals > pc_medals:
                    print(random.choice(phrases_ru_my))
                elif my_medals == pc_medals:
                    print('ÐÑƒÐ¶ÐµÐ½ Ñ€ÐµÐ²Ð°Ð½Ñˆ')
                else:
                    print(random.choice(phrases_ru_pc))
            elif my_answer == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ' or my_answer == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹' or my_answer == 'Ð±ÑƒÐ¼Ð°Ð³Ð°':
                answer_pc = random.choice(lis)
                print(f'{name_pc}: {answer_pc}')
                if answer_pc == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ' and my_answer == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ':
                    print('ÐÐ¸Ñ‡ÑŒÑ')
                elif answer_pc == 'Ð±ÑƒÐ¼Ð°Ð³Ð°' and my_answer == 'Ð±ÑƒÐ¼Ð°Ð³Ð°':
                    print('ÐÐ¸Ñ‡ÑŒÑ')
                elif answer_pc == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹' and my_answer == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹':
                    print('ÐÐ¸Ñ‡ÑŒÑ')
                    # if me win
                elif my_answer == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ' and answer_pc == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹':
                    print('Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð±ÐµÐ´Ð°')
                    my_medals.append('ðŸ…')
                elif my_answer == 'Ð±ÑƒÐ¼Ð°Ð³Ð°' and answer_pc == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ':
                    print('Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð±ÐµÐ´Ð°')
                    my_medals.append('ðŸ…')
                elif my_answer == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹' and answer_pc == 'Ð±ÑƒÐ¼Ð°Ð³Ð°':
                    print('Ð’Ð°ÑˆÐ° Ð¿Ð¾Ð±ÐµÐ´Ð°')
                    my_medals.append('ðŸ…')
                    # if PC win
                elif answer_pc == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ' and my_answer == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹':
                    print(f'ÐŸÐ¾Ð±ÐµÐ´Ð° {name_pc}')
                    pc_medals.append('ðŸ…')
                elif answer_pc == 'Ð±ÑƒÐ¼Ð°Ð³Ð°' and my_answer == 'ÐºÐ°Ð¼ÐµÐ½ÑŒ':
                    print(f'ÐŸÐ¾Ð±ÐµÐ´Ð° {name_pc}')
                    pc_medals.append('ðŸ…')
                elif answer_pc == 'Ð½Ð¾Ð¶Ð½Ð¸Ñ†Ñ‹' and my_answer == 'Ð±ÑƒÐ¼Ð°Ð³Ð°':
                    print(f'ÐŸÐ¾Ð±ÐµÐ´Ð° {name_pc}')
                    pc_medals.append('ðŸ…')
                game_with_pc()
            else:
                print('ÐŸÐ¾Ð¶Ð°Ð»ÑƒÐ¹ÑÑ‚Ð°, Ð²Ñ‹Ð±ÐµÑ€ÐµÑ‚Ðµ Ñ‚Ð¾Ð»ÑŒÐºÐ¾ Ð²Ñ‹ÑˆÐµÐ¿ÐµÑ€ÐµÑ‡Ð¸ÑÐ»ÐµÐ½Ð½Ñ‹Ðµ Ð¾Ñ‚Ð²ÐµÑ‚Ñ‹')
                game_with_pc()

        game_with_pc()
    else:
        print(f"I don't know that language(Ð¯ Ð½Ðµ Ð·Ð½Ð°ÑŽ ÑÑ‚Ð¾Ñ‚ ÑÐ·Ñ‹Ðº)\nTry again(ÐŸÐ¾Ð¿Ñ€Ð¾Ð±ÑƒÐ¹ ÑÐ½Ð¾Ð²Ð°)")
        lang()


lang()
input()