"""
Filter valid Wordle words based on user input for coded guesses
Makes use of regex
"""

from collections import defaultdict
from itertools import groupby
import re
import string
from tokenize import String

NUM_LETTERS = 5
RELATIVE_WORDLE_FILE_PATH = "wordle/wordle.txt"


def regex_builder(
    possible_letters: list, must_have_letters: defaultdict(int)
) -> String:
    """
    Builds a regex string that has lookahead for must have letters that do not have
    a determined position, then specifies the possible letters for each position
    e.g. (?=.*[g]{1})(?=.*[h].*[h])([c])([oa])([a-z])([a-z])([a-z])
    must have g & 2h in the word, with the following letters as specified by the char ranges
    """
    regex_str = ""
    for letter in must_have_letters:
        num_of_letters = f".*[{letter}]" * must_have_letters[letter]
        regex_str = regex_str + f"(?={num_of_letters})"
    for letters in possible_letters:
        regex_str = regex_str + f"[{letters}]"
    return regex_str


def multi_char_wrong_position(letter: str, guess: str, coded: str) -> int:
    """
    Determines if guess has multiple chars correct but in wrong position
    """
    id = 0
    count = 0
    for _ in range(guess.count(letter)):
        id = guess.index(letter, id)
        if coded[id] == "y":
            count += 1
        id += 1
    return count


def get_guess() -> tuple:
    "Return the Wordle guess and answer coded string"
    while True:
        guess_coded = input("Guess:coded(gyb)").partition(":")
        guess = guess_coded[0].lower()
        if len(guess) != NUM_LETTERS:
            print(f"Wrong number of letters in guess, found {len(guess)}")
            continue
        invalid_chars = re.findall(r"[^a-z]", guess)
        if invalid_chars:
            print(f"Invalid chars in guess, {''.join(invalid_chars)}")
            continue
        coded = guess_coded[2].lower()
        if len(coded) != NUM_LETTERS:
            print(f"Wrong number of codes in guess, found {len(coded)}")
            continue
        if any(char not in "gyb" for char in coded):
            print(f"Invalid char in {coded}, only g,y or b")
            continue
        return guess, coded


def get_wordle_list(filename: string) -> string:
    """return wordle file data"""
    with open(filename, "r") as fh:
        return fh.read()


def order_words(words: set) -> list:
    """Order words based on char frequency amongst remaining words"""
    word_score = defaultdict(int)
    letter_score = defaultdict(int)
    # frequency of letter in word set
    words_string = "".join(words)
    for char in string.ascii_lowercase:
        letter_score[char] = len(re.findall(char, words_string))
    for word in words:
        word_score[word] = 0
        for char in word:
            word_score[word] = word_score[word] + letter_score[char]
    return sorted(word_score.items(), key=lambda kv: kv[1], reverse=True)


def suggest_word(words: list) -> string:
    """Suggest a word based on frequency of characters"""
    od = order_words(words)
    try:
        while letter_repeated(suggestion := od.pop(0)[0]):
            print(f"Repeated Letters {suggestion}")
    except IndexError:
        print(f"End of list with {suggestion}")
    return suggestion


def letter_repeated(word: string) -> bool:
    """Check if word has multiple letters"""
    for letter, letter_seq in groupby(sorted(word)):
        if len(list(letter_seq)) > 1:
            return True
    return False


def main() -> None:
    """main"""

    words = get_wordle_list(RELATIVE_WORDLE_FILE_PATH)
    valid_letter_position = [string.ascii_lowercase] * NUM_LETTERS
    matched_words = []
    while not len(matched_words) == 1:
        must_have_letters = defaultdict(int)
        guess, coded = get_guess()
        for i, letter in enumerate(guess):
            if coded[i] == "b":
                for j in range(NUM_LETTERS):
                    if valid_letter_position[j] != letter:
                        valid_letter_position[j] = valid_letter_position[j].replace(
                            letter, ""
                        )
            elif coded[i] == "y":
                must_have_letters[letter] = multi_char_wrong_position(
                    letter, guess, coded
                )
                valid_letter_position[i] = valid_letter_position[i].replace(letter, "")
            elif coded[i] == "g":
                valid_letter_position[i] = letter
            else:
                pass
        regex = regex_builder(valid_letter_position, must_have_letters)
        matched_words = re.findall(regex, words)
        print(len(matched_words))
        print(matched_words)
        print(suggest_word(matched_words))


if __name__ == "__main__":
    main()
