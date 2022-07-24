"""
Testing Wordle general
"""

from wordle import letter_repeated, multi_char_wrong_position, order_words


def test_letter_repeated_false():
    """
    Testing letter_repeated false
    """
    assert letter_repeated("match") is False


def test_letter_repeated_true():
    """
    Testing letter_repeated true
    """
    assert letter_repeated("alpha") is True


def test_multi_char_wrong_position_a_balad():
    """
    Testing multi_char_wrong_position (alpha)
    """
    assert multi_char_wrong_position("a", "balad", "byyyb") == 2


def test_multi_char_wrong_position_l_balad():
    """
    Testing multi_char_wrong_position (alpha)
    """
    assert multi_char_wrong_position("l", "balad", "byyyb") == 1


def test_multi_char_wrong_position_a_alarm_gy():
    """
    Testing multi_char_wrong_position (alpha)
    """
    assert multi_char_wrong_position("a", "alarm", "ggybb") == 1


def test_multi_char_wrong_position_a_balad_gg():
    """
    Testing multi_char_wrong_position (alpha)
    """
    assert multi_char_wrong_position("a", "arena", "gbbbg") == 0


def test_order_words():
    """
    Testing multi_char_wrong_position (alpha)
    """
    unorderd_word_set = (
        "hairy",
        "alpha",
        "aired",
        "zebra",
        "bloom",
        "feist",
        "about",
        "clown",
        "crane",
        "black",
        "beige",
        "blink",
        "block",
    )

    ordered_word_score_list = [
        ("black", 28),
        ("zebra", 26),
        ("crane", 25),
        ("block", 25),
        ("aired", 24),
        ("blink", 24),
        ("about", 23),
        ("hairy", 20),
        ("bloom", 19),
        ("clown", 19),
        ("beige", 19),
        ("alpha", 17),
        ("feist", 15),
    ]

    assert order_words(unorderd_word_set) == ordered_word_score_list
