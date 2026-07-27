import binascii


def codificar(texto: str) -> str:
    """Codifica um texto em hexadecimal."""
    return texto.encode().hex()


def decodificar(codificado: str) -> str:
    """Decodifica um texto hexadecimal."""
    return binascii.unhexlify(codificado).decode()
