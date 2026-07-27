def cifrar(texto: str, chave: str) -> str:
    """Aplica cifra XOR usando uma chave.

    Args:
        texto: Texto original.
        chave: Chave para cifragem.

    Returns:
        str: Texto cifrado.
    """
    caracteres = []
    for i, c in enumerate(texto):
        caracteres.append(chr(ord(c) ^ ord(chave[i % len(chave)])))
    return "".join(caracteres)


def decifrar(texto: str, chave: str) -> str:
    """Decifra XOR (mesma operacao da cifragem)."""
    return cifrar(texto, chave)
