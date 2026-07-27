"""Testes para todas as cifras classicas (cifrar + decifrar roundtrip)."""

from braz.cifras import atbash, binario, cesar, morse, rot13, vigenere, xor


def test_cesar_roundtrip():
    original = "HELLO WORLD"
    deslocamento = 5
    cifrado = cesar.cifrar(original, deslocamento)
    assert cesar.decifrar(cifrado, deslocamento) == original


def test_cesar_mantem_maiusculas():
    assert cesar.cifrar("ABC", 1) == "BCD"


def test_cesar_mantem_minusculas():
    assert cesar.cifrar("abc", 1) == "bcd"


def test_cesar_mantem_nao_letras():
    assert cesar.cifrar("a b c", 1) == "b c d"


def test_rot13_roundtrip():
    original = "HELLO"
    assert rot13.decifrar(rot13.cifrar(original)) == original


def test_binario_roundtrip():
    original = "Hello"
    assert binario.decifrar(binario.cifrar(original)) == original


def test_morse_roundtrip():
    original = "SOS"
    assert morse.decifrar(morse.cifrar(original)) == original


def test_morse_com_espacos():
    original = "HELLO WORLD"
    assert morse.decifrar(morse.cifrar(original)) == original


def test_vigenere_roundtrip():
    original = "HELLO"
    chave = "KEY"
    assert vigenere.decifrar(vigenere.cifrar(original, chave), chave) == original


def test_vigenere_mantem_maiusculas():
    assert vigenere.cifrar("ABC", "B") == "BCD"


def test_atbash_roundtrip():
    original = "HELLO"
    assert atbash.decifrar(atbash.cifrar(original)) == original


def test_atbash_conhecido():
    assert atbash.cifrar("ABC") == "ZYX"


def test_xor_roundtrip():
    original = "Hello"
    chave = "key"
    assert xor.decifrar(xor.cifrar(original, chave), chave) == original


def test_xor_chave_maior_que_texto():
    original = "Hi"
    chave = "longkey"
    assert xor.decifrar(xor.cifrar(original, chave), chave) == original
