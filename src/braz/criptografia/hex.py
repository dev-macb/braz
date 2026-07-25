import binascii


def encode(texto: str) -> str:
    """Codifica um texto em hexadecimal."""
    return texto.encode().hex()


def decode(codificado: str) -> str:
    """Decodifica um texto hexadecimal."""
    return binascii.unhexlify(codificado).decode()
