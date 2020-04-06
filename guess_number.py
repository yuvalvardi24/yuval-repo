import random

playing = True
while playing:
    print('Welcome to the guessing game!')
    guessing = input('Would you like to guess or choose a number? Type "Guess" or "Choose" ')

    if guessing[0].lower() == 'g': # the user is guessing
        print('The user will be guessing!')
        print('Waiting for the computer to choose a random number between 1 and 100...')

        secret_num = random.randint(1,100)
        print('The computer chose a number between 1 and 100! Let\'s play!')

        human_guessing = True
        guess_counter = 0
        while human_guessing:
            guess = int(input('Please type in your guess: '))

            if guess < secret_num:
                print('Your guess is lower than the number.')
                guess_counter += 1
                continue
            elif guess > secret_num:
                print('Your guess is higher than the number.')
                guess_counter += 1
                continue
            else:
                guess_counter += 1
                print('Congrats! You got it right!')
                print(f'The computer chose {secret_num} and it took you {guess_counter} tries to get it!')
                human_guessing = False
                break

    elif guessing[0].lower() == 'c': # the user is choosing a number
        print('The computer will be guessing! ')
        secret_num = int(input('Please choose a number between 1 and 100: '))

        print('Computer guessing! Let\'s play!')
        computer_guessing = True
        guess_counter = 0
        guess_min = 1
        guess_max = 100
        #initialize the computer guess to be 1 so we can use it as a parameter for the loop.
        while computer_guessing:
            guess = round((guess_min + guess_max) / 2)
            print(f'The computer guessed {guess}.')

            if guess < secret_num:
                guess_counter += 1
                guess_min = guess
                print('Your guess is lower than the number!')
                continue
            elif guess > secret_num:
                guess_counter += 1
                guess_max = guess
                print('Your guess is higher than the number!')
                continue
            else:
                guess_counter += 1
                print('Congrats! You got it right!')
                print(f'You chose {secret_num} and it took the computer {guess_counter} to get it right! ')
                computer_guessing = False
                break
                #issue when the computer guesses the same number multiple times in a row

    else:
        print('Sorry, you need to enter "Guess" or "Choose. Please try again.')
        continue


    play_again = input('Would you like to play again? Type y or n ')

    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        playing = False
        print('Thanks for playing! See you again soon!')
        break

