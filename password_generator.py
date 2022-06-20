#!/usr/bin/env python3
import random
import string


def generate_pass(all_symbols, length):
    pool = ''

    for symbol_set in all_symbols:
        pool += symbol_set

    return ''.join(random.sample(pool, length))


def contains_all_symbols(all_symbols, gened_pass):
    bool_list = []
    for _ in all_symbols:
        bool_list.append(False)
    for char in gened_pass:
        for index, substring in enumerate(all_symbols):
            if char in substring:
                bool_list[index] = True
        if sum(bool_list) == len(all_symbols):
            return True
    return False


def main():
    symbols = [string.punctuation, string.ascii_lowercase, string.ascii_uppercase, string.digits]
    length = 0

    print('Welcome to minimalistic password generator!')

    try:
        length = int(input('\nEnter the length of password: '))
    except ValueError:
        print('Invalid input')
        exit()

    if length <= 0:
        raise Exception('Length can\'t be less than 1')

    answer = input('Do you want your password to contain necessarily at least 1 special character, lower and upper case latter and digit? (yes/no)\n')

    while answer != 'yes' and answer != 'no':
        answer = input('Invalid answer. Do you want your password to contain at least 1 special character, lower and upper case latter and digit? (yes/no)\n')

    if answer == 'yes':
        if length < 4:
            print('Your password length is too small')
            exit()
        else:
            password = generate_pass(symbols, length)
            while not contains_all_symbols(symbols, password):
                password = generate_pass(symbols, length)
    else:
        password = generate_pass(symbols, length)

    if length < 8:
        print('Your password is too weak, use it cautiously')
    elif length >= 8:
        print('\nIt\'s a pretty strong password, only quantum computer will crack it')
    print(f'Genereted password: {password}')


main()
