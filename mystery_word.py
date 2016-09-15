from string import ascii_lowercase
import random
with open("/usr/share/dict/words") as words_list:
    words_list = words_list.readlines()
    word = random.choice(words_list).upper()
    computer_word = list(word.strip("\n"))
    letter_count = 0
    alphabet = list(ascii_lowercase.upper())
    for letter in computer_word:
        letter_count += 1
    print ("You have 8 guesses to figure out the computer's hidden word")
    print ("This is how many letters the word contains:", letter_count)
    print (computer_word)
    blanks = list("_" * len(computer_word))
    guesses = 8
    bad_guesses = []
    while guesses >= 0 and blanks != computer_word:
        print (*alphabet)
        print (*blanks)
        print (bad_guesses)
        guess = input("Guess a letter: \n").upper()
        if guess in alphabet:
            alphabet.remove(guess)
        if guess in computer_word:
            print ("Well done!")
            if guess in blanks:
                print ("You have already guessed this letter")
        else:
            print ("Nope, try again")
            if guess in bad_guesses:
                print ("You have already guessed this letter")
            else:
                bad_guesses.append(guess)
                guesses -= 1
            print ("You have {} guesses remaining".format(guesses))


        for current_location, current_letter in enumerate(computer_word):
            if guess == current_letter:
                blanks[current_location] = guess
        if guesses == 0:
            print ("Game over. The word was {}".format(word))
            break
    if blanks == computer_word:
        print ("You have won the game! The word was {}".format(word))
