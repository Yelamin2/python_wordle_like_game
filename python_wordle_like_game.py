from pydoc import importfile
from random import randint
from os import system



# generate 5 letters word and give the user 6 tries to solve the game
#the user has to enter 5 letters which they can edit before submit
system('clear')
imported_list = open("word_list.txt", "r")
file_content = imported_list.readlines()
print("rrrrr",file_content[6], "ee")

def check_word():
    result_screen= ['','','','','']

    hidden_word = file_content[6].lower()
    entered_letters = input("Enter here").lower()
    letter_counter=0

    for char, word in zip(hidden_word, entered_letters):
        # print(letter_counter, type(word), result_screen)
        if word in hidden_word and word in char:
            result_screen[letter_counter]= word.upper()
            print("\033[92m {}\033[00m" .format(result_screen[letter_counter]), end='')
        elif word in hidden_word:
            result_screen[letter_counter]= word.upper()
            print("\033[93m {}\033[00m" .format(result_screen[letter_counter]), end='')
        else: 
            result_screen[letter_counter] = word.upper()
            print("\033[91m {}\033[00m" .format(result_screen[letter_counter]), end='')
        letter_counter= letter_counter+1
    result_screen= ''.join(result_screen).upper()

    print('\n',result_screen)            

playgame = check_word()
