# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
#from operator import truediv
#from os import PRIO_PGRP
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    #inFile = open(words.txt, 'r', 0)
    # line: string
    #line = inFile.readline()
    # wordlist: list of strings
    #wordlist = split(line)
    #print "  ", len(wordlist), "words loaded."
    #print 'Enter play_hangman() to play a game of hangman!'
    #return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
#words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    #word=words_dict[randrange(0,len(words_dict))]
    #return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap'
secret_word = list(secret_word)
letters_guessed = []
# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''

    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    guessed = False
    for x in letters_guessed:
        if x in secret_word:
            guessed = True
        else:
            guessed = False

    return guessed

correct_guesses = list("")
for x in secret_word:
        correct_guesses.append("-")
def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    str = ''
    global secret_word
    global letters_guessed
    global correct_guesses
    secret_word_list = list(secret_word)
    ####### YOUR CODE HERE ######
    
    for x in letters_guessed:
        for y in secret_word:
            if x == y:
                position = secret_word_list.index(y)
                correct_guesses[position] = x
                
    return str.join(correct_guesses)

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######
    mistakes_made = 0
    str = ''
    guessed = False
    guesses_made = MAX_GUESSES
    while True:
        print(guesses_made-mistakes_made, " mistakes left")
        print(str.join(correct_guesses))

        letter = input("Enter your guess: ")
        guessed = False

        for x in letters_guessed:
            if x == letter:
                guessed = True
                break

        if guessed:
            print("This letter has already been guessed. Plz try Again !!!")
            continue
        else:
            letters_guessed.append(letter)

        if word_guessed() and mistakes_made < MAX_GUESSES:
            print("Your guess was correct. ", mistakes_made, " mistakes have been made")
            letters_guessed_bool = print_guessed()
            print(letters_guessed_bool)

            completly_guessed = False
            word_guessed_list = list(letters_guessed_bool)
            for x in word_guessed_list:
                if x == '-':
                    completly_guessed = False
                    break
                else:
                    completly_guessed = True
        
            if completly_guessed:
                print("CONGRATULATIONS!!! YOU WON!!!")
                break
        else:
            mistakes_made+=1
            print("Your guess is wrong. ", mistakes_made, " mistakes have been made")

            if mistakes_made == MAX_GUESSES:
                print("SADGE !!! YOU LOOSE !!!")
                break

play_hangman()