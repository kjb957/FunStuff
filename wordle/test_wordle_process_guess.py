"""
Testing process_guess function
"""
from collections import defaultdict

from wordle import process_guess


def test_process_guess():
    """
    Testing score_word
    """
    guess = "igloo"
    coded = "bbyyb"
    valid_letter_position = [
        "bcdfghijkmnopqvwxz",
        "bcdfghijkmnpqvwxz",
        "bcdfghijklmnopqvwxz",
        "bcdfghijklmnopqvwxz",
        "bcdfghijklmnopqvwxz",
    ]
    valid_letter_position_processed = [
        "bcdfhjkmnopqvwxz",
        "bcdfhjkmnpqvwxz",
        "bcdfhjkmnopqvwxz",
        "bcdfhjklmnpqvwxz",
        "bcdfhjklmnpqvwxz",
    ]

    process_guess(guess, coded, defaultdict(int), valid_letter_position)
    assert valid_letter_position == valid_letter_position_processed
