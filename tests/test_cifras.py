"""Testes para todas as cifras classicas (encrypt + decrypt roundtrip)."""

from braz.cifras import atbash, binario, cesar, morse, rot13, vigenere, xor


def test_cesar_roundtrip():
    original = "HELLO WORLD"
    shift = 5
    cifrado = cesar.encrypt(original, shift)
    assert cesar.decrypt(cifrado, shift) == original


def test_cesar_mantem_maiusculas():
    assert cesar.encrypt("ABC", 1) == "BCD"


def test_cesar_mantem_minusculas():
    assert cesar.encrypt("abc", 1) == "bcd"


def test_cesar_mantem_nao_letras():
    assert cesar.encrypt("a b c", 1) == "b c d"


def test_rot13_roundtrip():
    original = "HELLO"
    assert rot13.decrypt(rot13.encrypt(original)) == original


def test_binario_roundtrip():
    original = "Hello"
    assert binario.decrypt(binario.encrypt(original)) == original


def test_morse_roundtrip():
    original = "SOS"
    assert morse.decrypt(morse.encrypt(original)) == original


def test_morse_com_espacos():
    original = "HELLO WORLD"
    assert morse.decrypt(morse.encrypt(original)) == original


def test_vigenere_roundtrip():
    original = "HELLO"
    chave = "KEY"
    assert vigenere.decrypt(vigenere.encrypt(original, chave), chave) == original


def test_vigenere_mantem_maiusculas():
    assert vigenere.encrypt("ABC", "B") == "BCD"


def test_atbash_roundtrip():
    original = "HELLO"
    assert atbash.decrypt(atbash.encrypt(original)) == original


def test_atbash_conhecido():
    assert atbash.encrypt("ABC") == "ZYX"


def test_xor_roundtrip():
    original = "Hello"
    chave = "key"
    assert xor.decrypt(xor.encrypt(original, chave), chave) == original


def test_xor_chave_maior_que_texto():
    original = "Hi"
    chave = "longkey"
    assert xor.decrypt(xor.encrypt(original, chave), chave) == original
