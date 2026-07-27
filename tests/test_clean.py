from braz.strings import clean


def test_remove_accents():
    assert clean.remove_accents("café") == "cafe"
    assert clean.remove_accents("São Paulo") == "Sao Paulo"


def test_remove_spaces():
    assert clean.remove_spaces("a b c") == "abc"


def test_remove_special_chars():
    assert clean.remove_special_chars("hello@world!") == "helloworld"


def test_apenas_digitos():
    assert clean.apenas_digitos("abc123def456") == "123456"


def test_apenas_letras():
    assert clean.apenas_letras("a1b2c3") == "abc"


def test_empty_string():
    assert clean.remove_accents("") == ""
    assert clean.remove_spaces("") == ""
    assert clean.apenas_digitos("") == ""
