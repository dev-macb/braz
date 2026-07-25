from braz.strings import utils


def test_slug():
    assert utils.slug("Olá Mundo!") == "ola-mundo"


def test_slug_sem_acentos():
    assert utils.slug("café com leite") == "cafe-com-leite"


def test_reverse():
    assert utils.reverse("abc") == "cba"


def test_reverse_empty():
    assert utils.reverse("") == ""


def test_count_chars():
    assert utils.count_chars("hello") == 5


def test_count_words():
    assert utils.count_words("hello world") == 2


def test_count_words_empty():
    assert utils.count_words("") == 0


def test_repeat():
    assert utils.repeat("ab", 3) == "ababab"


def test_truncate_curto():
    assert utils.truncate("hello", 10) == "hello"


def test_truncate_longo():
    assert utils.truncate("hello world", 5) == "hello..."


def test_pad():
    assert utils.pad("a", 5, ".") == "..a.."


def test_replace():
    assert utils.replace("hello world", "world", "there") == "hello there"
