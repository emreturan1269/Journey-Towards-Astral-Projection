
# Sprituality-Over-Rationality
# If you ever wondered what might lie beyond the reality we experience every day,
# This astral projection guideline might be just right for you!
# But you should first be familiar with your emotions in order to control them!

import random 
from collections import Counter 
  
someWords = '''sad happy frusturated joyful  
disgrace confused  shocked confident bored surprised excited tired jealous angry calm'''
  
someWords = someWords.split(' ') 
# randomly choose a secret word from our "someWords" LIST. 
word = random.choice(someWords)          
  
if __name__ == '__main__': 
    print('Guess the word! HINT: One of your everyday emotions') 
      
    for i in word: 
         # For printing the empty spaces for letters of the word 
        print('_', end = ' ')         
    print() 
  
    playing = True
     # list for storing the letters guessed by the player 
    letterGuessed = ''                 
    chances = len(word) + 2
    correct = 0
  
    try: 
        while (chances != 0): 
            print() 
            chances -= 1
  
            try: 
                guess = str(input('Enter a letter to guess: ')) 
            except: 
                print('Enter only a letter!') 
                continue
  
            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
  
            # If letter is guessed correcly 
            if guess in word: 
                letterGuessed += guess 
  
            # Print the word 
            for char in word: 
                if char in letterGuessed: 
                    print(char, end = ' ') 
                    correct += 1
                else: 
                    print('_', end = ' ') 
  
            # If user has guessed all the letters 
            if (Counter(letterGuessed) == Counter(word)): 
                print() 
                print('Congratulations, You won!') 
                break
  
        # If user has used all of his chances 
        if chances == 0: 
            print() 
            print('Efendim, çok beceriksizsiniz/ I am sorry:D') 
            print('The word was {}'.format(word)) 
  
    except KeyboardInterrupt: 
        print() 
        print('Bye! Try again.') 
        exit() 
  
        # print(letterGuessed) 
