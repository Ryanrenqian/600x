# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/lina/Canopy/600x/ProblemSet3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
secretWord=chooseWord(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lenth=len(secretWord)
    num=0
    for i in  secretWord:
        if i in lettersGuessed :
            num+=1
    if num == lenth:
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

#    lenth=len(secretWord)
    letters=''
    for i in secretWord:
        if i in lettersGuessed:
            letters+=i
        else:
            letters+='_'
    return letters


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    avletter=''
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lettersGuessed:
        if i in letters:
            letters.remove(i)
    for i in letters:
        avletter+=i
    return avletter
    


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
    print "Welcome to the game, Hangman!"
    num=8
    letters=''
    lenth=len(secretWord)
    available='abcdefghijklmnopqrstuvwxyz'
    lettersGuessed=[]
    print "I am thinking of a word that is "+str(lenth) +" letters long"
    while num!=0:
        if isWordGuessed(secretWord, lettersGuessed):
            return "Congratulations, you won!"
        print "You have "+str(num)+" guesses left."
        print "Available letters: "+str(available)
        letter=raw_input("please guess a letter:")
        lettersGuessed.append(letter)
#        letters=getGuessedWord(secretWord, lettersGuessed)
        
        if letter in available: 
            available=getAvailableLetters(lettersGuessed)
            if letter in secretWord:
                letters=getGuessedWord(secretWord, lettersGuessed)
                print "good guess:"+str(letters)
            else:
                print "Oops! That letter is not in my word:"+str(letters)
                num -=1
        else:
                print "Oops! You've already guessed that letter:"+str(letters)
        
        print "------------"
        if num==0:
            return "Sorry, you ran out of guesses. The word was else."
    
  




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
