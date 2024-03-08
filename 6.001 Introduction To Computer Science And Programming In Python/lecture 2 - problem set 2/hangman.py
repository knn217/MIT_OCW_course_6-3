# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #convert list to str
    guess = ''.join(letters_guessed)
    #compare these strings and return
    return (secret_word.lower() == guess.lower())



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # turn secret word's letters into '_'
    return_str = '_' * len(secret_word)
    # iterate through all letters in secret_word and letters_guessed
    for i in range(len(secret_word)):
        for letter in letters_guessed:
            # if the guessed letter match, replace the '_' at this index with the letter
            if secret_word[i].lower() == letter.lower():
                return_str = return_str[:i] + letter + return_str[i+1:]
                break
     
    return return_str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # get all available letters
    avail = string.ascii_lowercase
    # iterate through available letters and guessed letters
    for i in range(len(avail)):
        for letter in letters_guessed:
            # if there's a match, replace the current avail letter with '_'
            if avail[i].lower() == letter.lower():
                avail = avail[:i] + '_' + avail[i+1:]
                break
    # remove all '_' from available letters and return
    return avail.replace('_', '')
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # store these values first since we need to update them through the entire game
    guesses = 6
    warnings = 3
    letters_guessed = []
    # create a list for vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    guessed_str = '_' * len(secret_word)
    input_letter = '_'
    # anounce game start and inform players some info
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')  
    print('You have '+ str(warnings) + ' warnings left.')
    # game loops while guessed word is different from secret word
    while guessed_str != secret_word:
        # infinite loop for input that can only be broken out if input is legal
        while True:
            print('-------------')
            print('You have '+ str(guesses) + ' guesses left.')
            print('Available letters: ' + get_available_letters(letters_guessed))
            # prompt for input
            input_letter = input('Please guess a letter: ')
            # if input is in alphabetical
            if str.isalpha(input_letter):
                # warning for input repeat case
                if input_letter in letters_guessed:
                    # still warning(s) left
                    if warnings > 0:
                        warnings -= 1
                        print('Oops! You\'ve already guessed that letter. You have ' + str(warnings) + ' warnings left: ' + guessed_str)
                    # no more warnings
                    else:
                        warnings = 3
                        guesses -= 1
                        print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ' + guessed_str)
                # legal input, update guess and break out of infinite loop
                else:
                    letters_guessed += input_letter
                    break
            # if input is not alphabetical
            else:
                # still warning(s) left
                if warnings > 0:
                    warnings -= 1
                    print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left: ' + guessed_str)
                # no more warnings
                else:
                    warnings = 3
                    guesses -= 1
                    print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + guessed_str)
        
        # create guessed_str2 as the new letter_guessed
        guessed_str2 = get_guessed_word(secret_word, letters_guessed)
        # if new letter_guessed remains the same as old letter_guessed,
        # the guessed word does not appear in the secret word, so it's a miss
        if guessed_str == guessed_str2:
            print('Oops! That letter is not in my word: ' + guessed_str)
            # deplete guess chances differently for vowels 
            if input_letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
        # else, the guessed word does appear in the secret word, it's a good guess 
        else:
            guessed_str = guessed_str2
            print('Good guess: ' + guessed_str)
        # if guess chances reach 0, game over
        if guesses <= 0:
            guesses = 0
            print('Sorry, you ran out of guesses. The word was: ' + secret_word)
            break
    
    # if the game loop is broken out of and guess chances > 0, player won, calculate points
    if guesses > 0:
        print('Congratulations, you won!')
        print('Your total score for this game is: ' + str(guesses * len(set(secret_word))))
        
    

    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # if these wrd have different length, return False
    if len(my_word.strip()) != len(other_word.strip()):
        return False
    # iterate through my_word
    for i in range(len(my_word.strip())):
        # if the letter is '_', continue the loop
        if my_word[i] == '_':
            continue
        # if the letter is alphabetical, but different from other_word's same letter, return False
        elif my_word[i].lower() != other_word[i].lower():
            return False
    
    # if iterate through the entire word without a mismatch, return true
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # create an empty string 
    matches = ''
    
    # add any word that match with my_word into the empty string
    for match in wordlist:
        if match_with_gaps(my_word, match):
            matches += match + ' '
    
    # if the string is still empty, inform the player
    if matches == '':
        print('No matches found ')
    # if the string is no longer empty, print out the hints
    else:
        print(matches)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # store these values first since we need to update them through the entire game
    guesses = 6
    warnings = 3
    letters_guessed = []
    # create a list for vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    guessed_str = '_' * len(secret_word)
    input_letter = '_'
    # anounce game start and inform players some info
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')  
    print('You have '+ str(warnings) + ' warnings left.')
    # game loops while guessed word is different from secret word
    while guessed_str != secret_word:
        # infinite loop for input that can only be broken out if input is legal
        while True:
            print('-------------')
            print('You have '+ str(guesses) + ' guesses left.')
            print('Available letters: ' + get_available_letters(letters_guessed))
            # prompt for input
            input_letter = input('Please guess a letter: ')
            # if input is in alphabetical
            if str.isalpha(input_letter):
                # warning for input repeat case
                if input_letter in letters_guessed:
                    # still warning(s) left
                    if warnings > 0:
                        warnings -= 1
                        print('Oops! You\'ve already guessed that letter. You have ' + str(warnings) + ' warnings left: ' + guessed_str)
                    # no more warnings
                    else:
                        warnings = 3
                        guesses -= 1
                        print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess: ' + guessed_str)
                # legal input, update guess and break out of infinite loop
                else:
                    letters_guessed += input_letter
                    break
            # if input is not alphabetical
            else:
                # special case, player is looking for hint
                if input_letter == '*':
                    print('Possible word matches for ' + guessed_str + ' are: ')
                    show_possible_matches(guessed_str)
                # still warning(s) left
                elif warnings > 0:
                    warnings -= 1
                    print('Oops! That is not a valid letter. You have ' + str(warnings) + ' warnings left: ' + guessed_str)
                # no more warnings
                else:
                    warnings = 3
                    guesses -= 1
                    print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + guessed_str)

        # create guessed_str2 as the new letter_guessed
        guessed_str2 = get_guessed_word(secret_word, letters_guessed)
        # if new letter_guessed remains the same as old letter_guessed,
        # the guessed word does not appear in the secret word, so it's a miss
        if guessed_str == guessed_str2:
            print('Oops! That letter is not in my word: ' + guessed_str)
            # deplete guess chances differently for vowels 
            if input_letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
        # else, the guessed word does appear in the secret word, it's a good guess 
        else:
            guessed_str = guessed_str2
            print('Good guess: ' + guessed_str)
        # if guess chances reach 0, game over
        if guesses <= 0:
            guesses = 0
            print('Sorry, you ran out of guesses. The word was: ' + secret_word)
            break
    
    # if the game loop is broken out of and guess chances > 0, player won, calculate points
    if guesses > 0:
        print('Congratulations, you won!')
        print('Your total score for this game is: ' + str(guesses * len(set(secret_word))))
        



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #secret_word = 'apple'
    #hangman(secret_word)
    hangman_with_hints(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
