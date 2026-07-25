from braz.criptografia import url


def test_url_encode():
    assert url.encode("hello world") == "hello%20world"


def test_url_decode():
    assert url.decode("hello%20world") == "hello world"


def test_url_roundtrip():
    original = "a b c@d?"
    assert url.decode(url.encode(original)) == original
