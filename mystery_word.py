from string import ascii_lowercase
import random
def hangman_game():
    with open("/usr/share/dict/words") as words_list:
        words_list = words_list.readlines()
    level = input("Welcome to hangman! \n Select a difficulty: Easy Medium Hard \n")
    letter_count = 0
    alphabet = list(ascii_lowercase.upper())

    while True:
        word = random.choice(words_list).upper()
        computer_word = list(word.strip("\n"))
        if level == "Easy":
            num = [4, 5, 6]
            if len(computer_word) in num:
                break
            else:
                continue
        elif level == "Medium":
            num = [7, 8, 9, 10]
            if len(computer_word) in num:
                break
            else:
                continue
        elif level == "Hard":
            if len(computer_word) > 10:
                break
            else:
                continue
        else:
            print ("Not a valid option")
            hangman_game()
        break
    for letter in computer_word:
        letter_count += 1
    print ("You have 8 guesses to figure out the computer's hidden word")
    print ("This is how many letters the word contains:", letter_count)
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
        else:
            print ("Invalid guess")
        if guess in computer_word:
            print ("Well done! That letter is in the word")
        else:
            print ("That letter is not in the word")
            if guess not in bad_guesses:
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
    again = (input("Play again? y/n "))
    if again == "y":
        hangman_game()
    else:
        exit()
hangman_game()
