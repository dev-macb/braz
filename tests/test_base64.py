from braz.criptografia import base64


def test_base64_encode():
    assert base64.encode("Hello") == "SGVsbG8="


def test_base64_decode():
    assert base64.decode("SGVsbG8=") == "Hello"


def test_base64_roundtrip():
    original = "Hello World!"
    assert base64.decode(base64.encode(original)) == original


def test_base64_empty():
    assert base64.encode("") == ""
    assert base64.decode("") == ""
