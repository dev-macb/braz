def _caractere_atbash(c: str) -> str:
    if "A" <= c <= "Z":
        return chr(90 - (ord(c) - 65))
    if "a" <= c <= "z":
        return chr(122 - (ord(c) - 97))
    return c


def cifrar(texto: str) -> str:
    """Aplica a cifra Atbash (inverte o alfabeto)."""
    return "".join(_caractere_atbash(c) for c in texto)


def decifrar(texto: str) -> str:
    """Decifra Atbash (mesma operacao da cifragem)."""
    return cifrar(texto)
