import random
from Hangman_wordfile import words                 #importing other file for words
import string                           #for importing alphabet

def get_valid_word(words):              #define function
    word = random.choice(words)         #randomly chooses something from list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()                 #output in uppercase

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)            #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                #what the user has guessed


    #number of chances
    lives = 5

    #getting user input
    while len(word_letters) > 0 and lives > 0:                         #using while loop to let user keep guessing 
                                                         #when length of word is zero & lives are left then user has all letters of word
        #letters used to keep track
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left & You have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        # '-' for characters that aren't guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))        #take that list & join with space to create a string


        #primary code
        user_letter = input('Guess a letter: ').upper()     #guessing
        if user_letter in alphabet - used_letters:          #if its valid letter that is not used yet
            used_letters.add(user_letter)                   #adding it to used letter set
            if user_letter in word_letters:                 
                word_letters.remove(user_letter)            #if guessed letter matches from word than it gets removed

            else:
                lives = lives -1                            #takes away life if wrong
                print('Letter is not present.')
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')       #wrong guessed character

    #gets here when len(word_letters) == 0  OR when lives == 0; they exit loop
    if lives == 0:
        print('You died, Sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()
