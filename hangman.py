import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).lower()
    word_letters = set(word)
    #word_set = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    limit = 12
    while (len(word_letters)> 0) and (limit >0):

        print('You have guessed these letters: ',' '.join(used_letters))
        hint = [letter if letter in used_letters else '-' for letter in word]
        print("the actual word: ",' '.join(hint))


        user_letter = input('Guess a letter ')

        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)


        elif user_letter in used_letters:
            print('You have guessed that letter before!')
            continue
        
        else:
            print('You have entered an invalid input!')
            continue
        limit = limit - 1
        
    
    if len(word_letters)>0:
        print(f'Sorry!! the word was {word}')
    else:
        print(f'Hurray!! you guessed the word {word} correctly')


hangman()
    
