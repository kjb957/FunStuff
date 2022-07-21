"""
Testing regex_builder function
"""
from collections import defaultdict
import re

from pytest import fixture

from wordle import regex_builder, get_wordle_list, RELATIVE_WORDLE_FILE_PATH


@fixture(name="load_wordle_words")
def fixture_load_wordle_words():
    """
    Load the wordle data as a list of words
    """
    words = get_wordle_list(RELATIVE_WORDLE_FILE_PATH)
    return words


def test_regex_builder_crane_bbybb():
    """
    Testing regex_builder crane:bbybb
    """
    regex_str = (
        "(?=.*[a])"
        "[abdfghijklmopqstuvwxyz]"
        "[abdfghijklmopqstuvwxyz]"
        "[bdfghijklmopqstuvwxyz]"
        "[abdfghijklmopqstuvwxyz]"
        "[abdfghijklmopqstuvwxyz]"
    )
    valid_letter_position = [
        "abdfghijklmopqstuvwxyz",
        "abdfghijklmopqstuvwxyz",
        "bdfghijklmopqstuvwxyz",
        "abdfghijklmopqstuvwxyz",
        "abdfghijklmopqstuvwxyz",
    ]
    must_have_letters = defaultdict(int)
    must_have_letters["a"] = 1
    assert regex_builder(valid_letter_position, must_have_letters) == regex_str


def test_regex_builder_about_gbbbb():
    """
    Testing regex_builder about:gbbbb
    """
    regex_str = (
        "[a]"
        "[adfghijklmpqsvwxyz]"
        "[dfghijklmpqsvwxyz]"
        "[adfghijklmpqsvwxyz]"
        "[adfghijklmpqsvwxyz]"
    )
    valid_letter_position = [
        "a",
        "adfghijklmpqsvwxyz",
        "dfghijklmpqsvwxyz",
        "adfghijklmpqsvwxyz",
        "adfghijklmpqsvwxyz",
    ]
    must_have_letters = defaultdict(int)
    assert regex_builder(valid_letter_position, must_have_letters) == regex_str


def test_regex_builder_amply_gbybb():
    """
    Testing regex_builder amply:gbybb
    """
    regex_str = (
        "(?=.*[p])"
        "[a]"
        "[adfghijkpqsvwxz]"
        "[dfghijkqsvwxz]"
        "[adfghijkpqsvwxz]"
        "[adfghijkpqsvwxz]"
    )
    valid_letter_position = [
        "a",
        "adfghijkpqsvwxz",
        "dfghijkqsvwxz",
        "adfghijkpqsvwxz",
        "adfghijkpqsvwxz",
    ]
    must_have_letters = defaultdict(int)
    must_have_letters["p"] = 1
    assert regex_builder(valid_letter_position, must_have_letters) == regex_str


def test_regex_builder_sower_worse():
    """
    Testing regex_builder sower:ygyyy
    """
    regex_str = (
        "(?=.*[s])"
        "(?=.*[w])"
        "(?=.*[e])"
        "(?=.*[r])"
        "[abcdefghijklmnopqrtuvwxyz]"
        "[o]"
        "[abcdefghijklmnopqrstuvxyz]"
        "[abcdfghijklmnopqrstuvwxyz]"
        "[abcdefghijklmnopqstuvwxyz]"
    )
    valid_letter_position = [
        "abcdefghijklmnopqrtuvwxyz",
        "o",
        "abcdefghijklmnopqrstuvxyz",
        "abcdfghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqstuvwxyz",
    ]
    must_have_letters = defaultdict(int)
    must_have_letters["s"] = 1
    must_have_letters["w"] = 1
    must_have_letters["e"] = 1
    must_have_letters["r"] = 1
    assert regex_builder(valid_letter_position, must_have_letters) == regex_str


def test_find_words_worse(load_wordle_words):
    """
    Testing regex_find
    """
    regex_str = (
        "(?=.*[s])"
        "(?=.*[w])"
        "(?=.*[e])"
        "(?=.*[r])"
        "[abcdefghijklmnopqrtuvwxyz]"
        "[o]"
        "[abcdefghijklmnopqrstuvxyz]"
        "[abcdfghijklmnopqrstuvwxyz]"
        "[abcdefghijklmnopqstuvwxyz]"
    )

    assert re.findall(regex_str, load_wordle_words) == ["worse"]


def test_find_words_worse_morse(load_wordle_words):
    """
    Testing regex_find
    """
    regex_str = (
        "(?=.*[s])"
        "(?=.*[e])"
        "(?=.*[r])"
        "[hw]"
        "[o]"
        "[abcdefghijklmnopqrstuvxyz]"
        "[abcdfghijklmnopqrstuvwxyz]"
        "[abcdefghijklmnopqstuvwxyz]"
    )

    assert re.findall(regex_str, load_wordle_words) == ["horse", "worse"]


def test_find_words_smell(load_wordle_words):
    """
    Testing regex_find
    """
    regex_str = (
        "(?=.*[l].*[l])"
        "(?=.*[m])"
        "[bcdefghijkmnopqrstuvwxyz]"
        "[bcdefghijkmnopqrstuvwxyz]"
        "[bcdefghijklmnopqrstuvwxyz]"
        "[bcdefghijklnopqrstuvwxyz]"
        "[bcdefghijklmnopqrstuvwxyz]"
    )

    assert re.findall(regex_str, load_wordle_words) == ["smell"]


def test_find_words_bs_lly(load_wordle_words):
    """
    Testing regex_find
    """
    regex_str = (
        "(?=.*[l].*[l])"
        "[bs]"
        "[bcdefghijkmnopqrstuvwxyz]"
        "[bcdefghijklmnopqrstuvwxyz]"
        "[bcdefghijklnopqrstuvwxyz]"
        "[ly]"
    )
    assert re.findall(regex_str, load_wordle_words) == [
        "belly",
        "billy",
        "bully",
        "shell",
        "silly",
        "skill",
        "skull",
        "smell",
        "spell",
        "spill",
        "still",
        "sully",
        "swell",
        "swill",
    ]


def test_find_words_bs_u_lly(load_wordle_words):
    """
    Testing regex_find
    """
    regex_str = (
        "(?=.*[l].*[l])"
        "(?=.*[u])"
        "[bs]"
        "[bcdefghijkmnopqrstuvwxyz]"
        "[bcdefghijklmnopqrstuvwxyz]"
        "[bcdefghijklnopqrstuvwxyz]"
        "[ly]"
    )
    assert re.findall(regex_str, load_wordle_words) == [
        "bully",
        "skull",
        "sully",
    ]
