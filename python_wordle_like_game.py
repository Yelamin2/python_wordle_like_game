from pydoc import importfile
from random import randint
from os import system
from typing import List
from webbrowser import get


system('clear')

imported_list = open("word_list.txt", "r")
file_content = imported_list.readlines()
result_counter=0
other_screen=[[],[],[],[],[]]

class Game_Start():
    def __init__(self):
        print('')


    # generate 5 letters word and give the user 6 tries to solve the game
    #the user has to enter 5 letters which they can edit before submit
    # imported_list = open("word_list.txt", "r")
    # file_content = imported_list.readlines()
    
    

    def enter_word(self):
        print("Enter 5 letters word")
        entered_letters = input("-->>").lower()
        self.entered_letters = entered_letters
        # print(len(self.entered_letters))
        return self.entered_letters
        


    def check_input(self):
        print("ff", result_counter)
        if len(self.entered_letters) == 5:
            # print(self.entered_letters)
            self.entered_letters
            
        
        else:
            print('Enter only 5 letters words')
            self.enter_word()
        
        self.check_word()


    def check_word(self):
        global result_counter, other_screen

        plr = result_counter
        print(plr)
        result_screen= ['','','','','']
        
        
    
        self.hidden_word = file_content[6].lower()
        # self.entered_letters = input("Enter here").lower()
        letter_counter=0
        

        for char, word in zip(self.hidden_word, self.entered_letters):
            # print(letter_counter, type(word), result_screen)
            if word in self.hidden_word and word in char:
                result_screen[letter_counter]= word.upper()
                print("\033[92m {}\033[00m" .format(result_screen[letter_counter]), end='')
            elif word in self.hidden_word:
                result_screen[letter_counter]= word.upper()
                print("\033[93m {}\033[00m" .format(result_screen[letter_counter]), end='')
            else: 
                result_screen[letter_counter] = word.upper()
                print("\033[91m {}\033[00m" .format(result_screen[letter_counter]), end='')
            letter_counter= letter_counter+1
        result_screen= ''.join(result_screen).upper()
        other_screen[plr]= result_screen
        # global result_counter
        result_counter= result_counter+1
        print(other_screen)

        



        print('\n',result_screen )
        

def play_Game():
    play_game = Game_Start()
    while result_counter<5:
        play_game.enter_word()
        play_game.check_input()
    # play_game.check_word()
    
               

play_Game()
