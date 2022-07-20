import string
import re
from collections import defaultdict
from wordle import (
    RELATIVE_WORDLE_FILE_PATH,
    NUM_LETTERS,
    get_wordle_list,
    process_guess,
    regex_builder,
    suggest_word,
    score_word,
)

WORDLE_WORD_STR = get_wordle_list(RELATIVE_WORDLE_FILE_PATH)
WORDLE_WORDS = WORDLE_WORD_STR.split()
STARTING_WORD = "rouse"


def guess_word(word_to_guess: string, initial_guess: string = None) -> None:
    """Guess the current word"""

    valid_letter_position = [string.ascii_lowercase] * NUM_LETTERS
    matched_words = WORDLE_WORDS
    guess_count = 1
    guess = initial_guess if initial_guess else suggest_word(matched_words)
    while not len(matched_words) == 1:
        guess_count += 1
        must_have_letters = defaultdict(int)
        coded = score_word(guess, word_to_guess)
        process_guess(guess, coded, must_have_letters, valid_letter_position)
        matched_words = re.findall(
            regex_builder(valid_letter_position, must_have_letters), WORDLE_WORD_STR
        )
        guess = suggest_word(matched_words)
    return guess_count


def main() -> None:
    """Main"""
    print(STARTING_WORD)
    wordle_guess_count = defaultdict(int)
    count_stats = defaultdict(int)
    for word_to_guess in WORDLE_WORDS:
        guess_count = guess_word(word_to_guess, STARTING_WORD)
        wordle_guess_count[word_to_guess] = guess_count
        count_stats[guess_count] += 1
    print(count_stats)


if __name__ == "__main__":
    main()
