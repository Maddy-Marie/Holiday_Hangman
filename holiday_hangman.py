
#Welcome Messages
print('Welcome to Holiday Hangman!')
print('The rules are simple: the computer will pick a holiday-themed word and set places for the letters.')
print('After that, it\'s up to you to guess the letter or word!')
print()
print('If you guess the wrong letter or word, a line will be added to the figure.')
print()
print('Be careful-you only have 6 tries! Good Luck!')
print('\n')
print('\n')


#Hangman display
def hangman(wrong):
    stages = [
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """
            ]
    return stages[wrong]


#import random
import random


#easy mode words
easy_words = ['snow','hot cocoa','holly','star','tree','bells','silver','gold','carol','noel','elves','sled','toys','gifts','cold']

#medium mode words
medium_words = ['snowing','wreath','ribbon','festive','family','happy holidays','tinsel','chimney','eggnog','mittens','sleigh rides','tidings','candles']

#hard mode words
hard_words = ['ornaments','celebration','decorations','mistletoe','tannenbaum','stockings','gingerbread house','nutcracker','poinsettia','goodwill','sleighbells','snowflakes','carolling']


#function to get word
def choose_word(easy_words, medium_words, hard_words):
    user_input = input('Choose difficulty level: Easy (e), Medium (m), or Hard (h): ').upper()
    #if_statement to get word from wanted group
    if user_input == 'E':
        choice = random.choice(easy_words)
    elif user_input == 'M':
        choice = random.choice(medium_words)
    else:
        choice = random.choice(hard_words)
    #check for spaces and print the hint statement
    res = ' ' in choice
    if res == True:
        print('Watch out-there are spaces in this one. *hint: use a space as a try!*', '\n')
            
      
    word = choice.upper()
    return word


def play(word):
    #set variables
    guessed = False
    completed_word = '-'*len(word)
    guessed_letters = []
    guessed_words = []
    wrong = 0
    word_length = len(word)
    

    
    #print hangman display and what's left of the word
    print(completed_word)
    print('The word is ',word_length,'letters long.')
    print(hangman(wrong))
    print('\n')

    #While loop that plays the game
    while not guessed and wrong < 6:
        guess = input('Please guess a letter or word: ').upper()

        if len(guess) == 1 and guess.isalpha:
            #checks all possible outcomes of entered LETTERS
            if guess not in word:
                print(guess, 'is not in the word')
                guessed_letters.append(guess)
                wrong += 1
            elif guess in guessed_letters:
                print('You already guessed that letter!')
            else:
                print('Congrats!', guess, 'is in the word!')
                guessed_letters.append(guess)
                #updates the underscores
                wordlist = list(completed_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for i in indices:
                    wordlist[i] = guess
                completed_word = ''.join(wordlist)
                if '-' not in completed_word:
                    guessed = True
                

                
                
        #checks all possible ocutomes of entered WORDS
        elif len(guess) == len(word) and guess.isalpha:
            if guess in guessed_words:
                print('You already guessed that word!')
            elif guess != word:
                print(guess,' isn\'t the word')
                guessed_words.append(guess)
                wrong += 1
            else:
                guessed = True
                completed_word = word


        #checks invalid answers
        else:
            print('Not a valid guess')

        print(hangman(wrong))
        print(completed_word)
        print('\n')
        
    #prints final statements
    if guessed:
        print('Congratulations, you guessed the word! Happy Holidays!')
    else:
        print('You ran out of tries. The word was '+word+'. Better luck next time')
        
#main function
def main():
    word = choose_word(easy_words, medium_words, hard_words)
    play(word)
    #allows for the game to be played multiple times
    while input('Play again? Yes (y) or No (n): ').upper() == 'Y':
        word = choose_word(easy_words, medium_words, hard_words)
        play(word)
        
if __name__ == "__main__":
    main()
    

    
