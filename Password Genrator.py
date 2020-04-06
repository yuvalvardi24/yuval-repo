import string
from random import sample
import random

#take in lowercase, uppercase, digits, special characters
# use those to generate the password

letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
numbers = string.digits
special_chars = string.punctuation

def pass_gen(lower = letters_lower, upper = letters_upper ,numbers = numbers ,special = special_chars):
    new_pass = True

    while new_pass:
        user_input = input('Enter a list of 4 numbers separated by space.'
                           '\nThe first number will be the number of lowercase letters in your pass.'
                           '\nThe second number will be the number of uppercase letters in your pass.'
                           '\nThe third number will be the number of digits in your pass.'
                           '\nFinally, the fourth number will be the number of special characters in your pass: ')

        user_list = user_input.split()
        print(f'You chose {user_list}.')
        print(f'Meaning, you chose'
              f'\n{int(user_list[0])} lowercase letters,'
              f'\n{int(user_list[1])} uppercase letters,'
              f'\n{int(user_list[2])} digits,'
              f'\n{int(user_list[3])} special characters.')
        if int(user_list[0]) > len(lower):
            print(f'Sorry, the max number of lowercase letters you can have is {len(lower)}. Please try again.')
            continue
        elif int(user_list[1]) > len(upper):
            print(f'Sorry, the max number of uppercase letters you can have is {len(upper)}. Please try again.')
            continue
        elif int(user_list[2]) > len(numbers):
            print(f'Sorry, the max number of digits you can have is {len(numbers)}. Please try again.')
            continue
        elif int(user_list[3]) > len(special):
            print(f'Sorry, the max number of special characters you can have is {len(special)}. Please try again.')
            continue
        else:
            user_pass = []

            lower_pass = sample(lower, int(user_list[0]))
            user_pass.extend(lower_pass)
            upper_pass = sample(upper, int(user_list[1]))
            user_pass.extend(upper_pass)
            num_pass = sample(numbers, int(user_list[2]))
            user_pass.extend(num_pass)
            spec_pass = sample(special, int(user_list[3]))
            user_pass.extend(spec_pass)


            random.shuffle(user_pass)
            password = ''.join(map(str,user_pass))

            print(f'The program generated a password for you, which is {password} ')
            prompt = input('Would you like another password? y or n ')

            if prompt[0].lower() == 'y':
                continue
            else:
                new_pass = False
                return f'Your password is {password}'

print(pass_gen())

# At the moment, the program only allows for 1 of every character (no repetitions)
# Fix the program to allow repetitions of letters/digits/special characters