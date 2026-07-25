def _atbash_char(c: str) -> str:
    if "A" <= c <= "Z":
        return chr(90 - (ord(c) - 65))
    if "a" <= c <= "z":
        return chr(122 - (ord(c) - 97))
    return c


def encrypt(texto: str) -> str:
    """Aplica a cifra Atbash (inverte o alfabeto)."""
    return "".join(_atbash_char(c) for c in texto)


def decrypt(texto: str) -> str:
    """Decifra Atbash (mesma operacao da cifragem)."""
    return encrypt(texto)
