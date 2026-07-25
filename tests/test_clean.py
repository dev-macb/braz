from braz.strings import clean


def test_remove_accents():
    assert clean.remove_accents("café") == "cafe"
    assert clean.remove_accents("São Paulo") == "Sao Paulo"


def test_remove_spaces():
    assert clean.remove_spaces("a b c") == "abc"


def test_remove_special_chars():
    assert clean.remove_special_chars("hello@world!") == "helloworld"


def test_only_digits():
    assert clean.only_digits("abc123def456") == "123456"


def test_only_letters():
    assert clean.only_letters("a1b2c3") == "abc"


def test_empty_string():
    assert clean.remove_accents("") == ""
    assert clean.remove_spaces("") == ""
    assert clean.only_digits("") == ""
