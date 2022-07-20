from collections import defaultdict
from wordle import score_word, process_guess

def test_score_word_all_match():
    assert score_word("match", "match") == "ggggg"

def test_score_word_first_char_match():
    assert score_word("mwxyz", "match") == "gbbbb"

def test_score_word_first_and_last_char_match():
    assert score_word("mxyzh", "match") == "gbbbg"

def test_score_word_first_char_match_2nd_char_wrong_position():
    assert score_word("mtxyz", "match") == "gybbb"

def test_score_word_first_char_match_2nd_char_wrong_position_fifth_char_dupof_first():
    assert score_word("mtxym", "match") == "gybbb"

def test_score_word_double_char_correct():
    assert score_word("ghoss", "glass") == "gbbgg"

def test_score_word_double_char_correct_with_third_not():
    assert score_word("shoss", "glass") == "bbbgg"

def test_score_word_all_yellow():
    assert score_word("sslag", "glass") == "yyyyy"

def test_score_word_no_match():
    assert score_word("vwxyz", "match") == "bbbbb"

def test_score_word_check_alert_aback():
    assert score_word("alert", "aback") == "gbbbb"

def test_score_word_check_igloo_knoll():
    assert score_word("igloo", "knoll") == "bbyyb"

def test_process_guess():
    guess = "igloo"
    coded = "bbyyb"
    valid_letter_position = [
        'bcdfghijkmnopqvwxz',
        'bcdfghijkmnpqvwxz',
        'bcdfghijklmnopqvwxz',
        'bcdfghijklmnopqvwxz',
        'bcdfghijklmnopqvwxz'
        ]
    valid_letter_position_processed = [
        'bcdfhjkmnopqvwxz',
        'bcdfhjkmnpqvwxz',
        'bcdfhjkmnopqvwxz',
        'bcdfhjklmnpqvwxz',
        'bcdfhjklmnpqvwxz'
        ]

    process_guess(guess, coded, defaultdict(int), valid_letter_position)
    assert valid_letter_position == valid_letter_position_processed