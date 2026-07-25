def encrypt(texto: str, chave: str) -> str:
    """Aplica cifra XOR usando uma chave.

    Args:
        texto: Texto original.
        chave: Chave para cifragem.

    Returns:
        str: Texto cifrado.
    """
    chars = []
    for i, c in enumerate(texto):
        chars.append(chr(ord(c) ^ ord(chave[i % len(chave)])))
    return "".join(chars)


def decrypt(texto: str, chave: str) -> str:
    """Decifra XOR (mesma operacao da cifragem)."""
    return encrypt(texto, chave)
