import re
import string
from collections import defaultdict

def regex_builder(possible_letters):
    """Builds"""
    regex_str = ''
    for letter in possible_letters.values():
        regex_str = regex_str + f'[{"".join(letter)}]'
    return regex_str

with open('wordle.txt', 'r') as fh:
    words = fh.read()

correct_word = False
valid_letter_position = defaultdict(list)
for i in range(5):
    valid_letter_position[i] = list(string.ascii_lowercase)

while not correct_word:
    guess_coded = input("Guess:coded(gyb)").partition(':')
    guess = guess_coded[0].lower()
    coded = guess_coded[2].lower()
    for i, letter in enumerate(guess):   
        if coded[i] == 'b':
            for j in range(4):
                if letter in valid_letter_position[j]:
                    valid_letter_position[j].remove(letter)
        elif coded[i] == 'y':
            if letter in valid_letter_position[i]:
                valid_letter_position[i].remove(letter)
        elif coded[i] == 'g':
            valid_letter_position[i] = [letter]
        else:
            pass
    regex = regex_builder(valid_letter_position)
    match = re.findall(regex, words)
    print(len(match))
    print(match)




        




    
