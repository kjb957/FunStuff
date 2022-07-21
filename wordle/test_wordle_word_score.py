"""
Testing score_word function
"""

from wordle import score_word


def test_score_word_all_match():
    """
    Testing score_word
    """
    assert score_word("match", "match") == "ggggg"


def test_score_word_first_char_match():
    """
    Testing score_word
    """
    assert score_word("mwxyz", "match") == "gbbbb"


def test_score_word_first_and_last_char_match():
    """
    Testing score_word
    """
    assert score_word("mxyzh", "match") == "gbbbg"


def test_score_word_first_char_match_2nd_char_wrong_position():
    """
    Testing score_word
    """
    assert score_word("mtxyz", "match") == "gybbb"


def test_score_word_first_char_match_2nd_char_wrong_position_fifth_char_dupof_first():
    """
    Testing score_word
    """
    assert score_word("mtxym", "match") == "gybbb"


def test_score_word_double_char_correct():
    """
    Testing score_word
    """
    assert score_word("ghoss", "glass") == "gbbgg"


def test_score_word_double_char_correct_with_third_not():
    """
    Testing score_word
    """
    assert score_word("shoss", "glass") == "bbbgg"


def test_score_word_all_yellow():
    """
    Testing score_word
    """
    assert score_word("sslag", "glass") == "yyyyy"


def test_score_word_no_match():
    """
    Testing score_word
    """
    assert score_word("vwxyz", "match") == "bbbbb"


def test_score_word_check_alert_aback():
    """
    Testing score_word
    """
    assert score_word("alert", "aback") == "gbbbb"


def test_score_word_check_igloo_knoll():
    """
    Testing score_word
    """
    assert score_word("igloo", "knoll") == "bbyyb"
