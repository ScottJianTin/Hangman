from words import words
import random
import string


def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    used_letter = set()
    word = get_valid_word(words)
    letter = set(word)
    alphabet = set(string.ascii_uppercase)
    lives = 10

    while len(letter) > 0 and lives > 0:
        print('\nCurrent lives: {}'.format(lives))

        print('Used letter:', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Enter a letter: ').upper()

        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in letter:
                letter.remove(user_letter)
            else:
                lives -= 1
                print('Wrong character. Try again')

        elif user_letter in used_letter:
            print('Repeated letter. Try a different letter.')

        else:
            print('Invalid character.')

    if lives == 0:
        print('You lose. Try again')
    else:
        print('Congratulations. You have guessed the correct word ({})'.format(word))


hangman()
