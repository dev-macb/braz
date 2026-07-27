import base64 as _base64


def codificar(texto: str) -> str:
    """Codifica um texto em Base64."""
    return _base64.b64encode(texto.encode()).decode()


def decodificar(codificado: str) -> str:
    """Decodifica um texto em Base64."""
    return _base64.b64decode(codificado).decode()
