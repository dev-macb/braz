from braz.criptografia import hex


def test_hex_codificar():
    assert hex.codificar("Hello") == "48656c6c6f"


def test_hex_decodificar():
    assert hex.decodificar("48656c6c6f") == "Hello"


def test_hex_roundtrip():
    original = "Hello World!"
    assert hex.decodificar(hex.codificar(original)) == original


def test_hex_empty():
    assert hex.codificar("") == ""
