from braz.criptografia import base64


def test_base64_codificar():
    assert base64.codificar("Hello") == "SGVsbG8="


def test_base64_decodificar():
    assert base64.decodificar("SGVsbG8=") == "Hello"


def test_base64_roundtrip():
    original = "Hello World!"
    assert base64.decodificar(base64.codificar(original)) == original


def test_base64_empty():
    assert base64.codificar("") == ""
    assert base64.decodificar("") == ""
