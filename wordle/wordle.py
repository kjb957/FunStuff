import re
import string
import copy

def regex_builder(possible_letters):
    """Builds"""
    regex_str = ''
    for letters in possible_letters:
        regex_str = regex_str + f'[{letters}]'
    return regex_str

with open('wordle/wordle.txt', 'r') as fh:
    words = fh.read()

correct_word = False
valid_letter_position = [string.ascii_lowercase] * 5
must_have_letters = []
match = []
while not len(match) == 1:
    guess_coded = input("Guess:coded(gyb)").partition(':')
    guess = guess_coded[0].lower()
    coded = guess_coded[2].lower()
    for i, letter in enumerate(guess):   
        if coded[i] == 'b':
            for j in range(4):
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
    




        




    
