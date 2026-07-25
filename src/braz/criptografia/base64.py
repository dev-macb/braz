import base64 as _base64


def encode(texto: str) -> str:
    """Codifica um texto em Base64."""
    return _base64.b64encode(texto.encode()).decode()


def decode(codificado: str) -> str:
    """Decodifica um texto em Base64."""
    return _base64.b64decode(codificado).decode()
