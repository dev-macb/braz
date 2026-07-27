import codecs


def cifrar(texto: str) -> str:
    """Aplica ROT13 em um texto."""
    return codecs.encode(texto, "rot_13")


def decifrar(texto: str) -> str:
    """Decifra ROT13 (mesmo que criptografar)."""
    return codecs.encode(texto, "rot_13")
