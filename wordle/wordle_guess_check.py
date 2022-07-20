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
    score_word
    )

WORDLE_WORD_STR = get_wordle_list(RELATIVE_WORDLE_FILE_PATH)
WORDLE_WORDS = WORDLE_WORD_STR.split()
STARTING_WORD = "crane"


def guess_word(word_to_guess: string) -> None:
    """Guess the current word"""

    valid_letter_position = [string.ascii_lowercase] * NUM_LETTERS
    matched_words = WORDLE_WORDS
    guess_count = 1
    guess = "crane"
    while not len(matched_words) == 1:
        guess_count += 1
        must_have_letters = defaultdict(int)
        if guess_count != 2:
            guess = suggest_word(matched_words)
        coded = score_word(guess, word_to_guess)
        process_guess(guess, coded, must_have_letters, valid_letter_position)

        regex = regex_builder(valid_letter_position, must_have_letters)
        matched_words = re.findall(regex, WORDLE_WORD_STR)
        # print(len(matched_words))
        # print(matched_words)
        # print(suggest_word(matched_words))
    return guess_count


def main() -> None:
    """Main"""
    print(suggest_word(WORDLE_WORDS))
    wordle_guess_count = defaultdict(int)
    count_stats = defaultdict(int)
    for word_to_guess in WORDLE_WORDS:
        guess_count = guess_word(word_to_guess)
        wordle_guess_count[word_to_guess] = guess_count
        count_stats[guess_count] += 1
        if guess_count == 1:
            print(guess_count, word_to_guess)
    print(count_stats)


if __name__ == "__main__":
    main()