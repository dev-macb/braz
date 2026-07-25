def _vigenere(texto: str, chave: str, direction: int) -> str:
    result = []
    key_idx = 0
    for c in texto:
        if "A" <= c <= "Z":
            shift = ord(chave[key_idx % len(chave)].upper()) - 65
            result.append(chr((ord(c) - 65 + shift * direction) % 26 + 65))
            key_idx += 1
        elif "a" <= c <= "z":
            shift = ord(chave[key_idx % len(chave)].upper()) - 65
            result.append(chr((ord(c) - 97 + shift * direction) % 26 + 97))
            key_idx += 1
        else:
            result.append(c)
    return "".join(result)


def encrypt(texto: str, chave: str) -> str:
    """Aplica a cifra de Vigenere.

    Args:
        texto: Texto original.
        chave: Palavra-chave para cifragem.

    Returns:
        str: Texto cifrado.
    """
    return _vigenere(texto, chave, 1)


def decrypt(texto: str, chave: str) -> str:
    """Decifra um texto cifrado com Vigenere.

    Args:
        texto: Texto cifrado.
        chave: Palavra-chave utilizada na cifragem.

    Returns:
        str: Texto decifrado.
    """
    return _vigenere(texto, chave, -1)
