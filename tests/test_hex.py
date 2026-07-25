from braz.criptografia import hex


def test_hex_encode():
    assert hex.encode("Hello") == "48656c6c6f"


def test_hex_decode():
    assert hex.decode("48656c6c6f") == "Hello"


def test_hex_roundtrip():
    original = "Hello World!"
    assert hex.decode(hex.encode(original)) == original


def test_hex_empty():
    assert hex.encode("") == ""
