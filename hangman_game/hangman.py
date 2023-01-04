# Hangman game
####Note####
# -----------------------------------
#
#My addition to the existing code is under
# "FILL IN YOUR CODE HERE..."
#The structure of the program was provided by my instructor.
#It was my responsibility to fill in the problems
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    
    #have length of answer
    #if there arent len(answer) confirmed responses return false
        
    count = 0
    for c in secretWord:
        
        if c in lettersGuessed:
            count += 1
            
    if count == len(secretWord):
        return True 
    else:
        return False
        
        
    
    




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    #if letter is in list, append letter 
    #else, append underscore 
    output = ''
    for c in secretWord:
        
        if c not in lettersGuessed:
            output += '_ '
        else: 
            output += (c)
            
    
    return(str(output))



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string

    alpha = str(string.ascii_lowercase)
    an = ''
    
    for a in alpha:
        if a not in lettersGuessed:
            an += a
            
    
    return(an)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    
    
    len_s = len(secretWord)
    
    print("Hello! Let's play a game.")
    print('There are '+ str(len_s) + " letters in a secret word\tIt's your job to guess it!")
    print('You have 8 attempts to guess the word ... \n Correct guesses will NOT be counted against you!')
        
       
    lettersGuessed = ''
    
    x = 8
    while(x != 0):
        guess = input('Enter a letter to see if it is in the word: ')

        if guess in lettersGuessed:
            print("\nWhoops! It seems you have already guessed that letter.\n")


        elif guess in secretWord:
            print('\nWow! That was a good guess!\n')
            lettersGuessed += guess


        else:
            x -= 1
            lettersGuessed += guess
        if (isWordGuessed(secretWord, lettersGuessed)):
            print('Well done! You have guessed the word: '+ secretWord)
            break

        print("-You have guessed: " + getGuessedWord(secretWord, lettersGuessed) +'\n')
        print("-Letters remaining: " + getAvailableLetters(lettersGuessed) +'\n')
        print("-You have " + str(x) + ' guesses remaining')   

    if x == 0:
        print("The secret word was "+ secretWord + ". Better luck next time!")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
