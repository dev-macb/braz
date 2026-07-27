from braz.criptografia import url


def test_url_codificar():
    assert url.codificar("hello world") == "hello%20world"


def test_url_decodificar():
    assert url.decodificar("hello%20world") == "hello world"


def test_url_roundtrip():
    original = "a b c@d?"
    assert url.decodificar(url.codificar(original)) == original
