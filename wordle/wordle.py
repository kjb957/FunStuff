import re
import string
import copy

NUM_LETTERS = 5

def regex_builder(possible_letters):
    """Builds"""
    regex_str = ''
    for letters in possible_letters:
        regex_str = regex_str + f'[{letters}]'
    return regex_str

with open('wordle/wordle.txt', 'r') as fh:
    words = fh.read()

valid_letter_position = [string.ascii_lowercase] * NUM_LETTERS
must_have_letters = []
match = []
while not len(match) == 1:
    guess_coded = input("Guess:coded(gyb)").partition(':')
    guess = guess_coded[0].lower()
    if len(guess) != NUM_LETTERS:
        print(f'Wrong number of letters in guess, found {len(guess)}')
        continue
    coded = guess_coded[2].lower()
    if any(char not in 'gyb' for char in coded):
        print(f'Invalid char in {coded}, only g,y or b')
        continue
    for i, letter in enumerate(guess):   
        if coded[i] == 'b':
            for j in range(NUM_LETTERS):
                valid_letter_position[j] = valid_letter_position[j].replace(letter, '')
        elif coded[i] == 'y':
            if letter not in must_have_letters:
                must_have_letters.append(letter)
            valid_letter_position[i] = valid_letter_position[i].replace(letter, '')
        elif coded[i] == 'g':
            valid_letter_position[i] = letter
        else:
            pass
    regex = regex_builder(valid_letter_position)
    match = re.findall(regex, words)
    for word in copy.deepcopy(match):
        for letter in must_have_letters:
            if letter not in word:
                match.remove(word)
    print(len(match))
    print(match)
    




        




    
