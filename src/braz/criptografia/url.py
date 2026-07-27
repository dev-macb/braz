import urllib.parse


def codificar(texto: str) -> str:
    """Codifica um texto para URL encoding."""
    return urllib.parse.quote(texto)


def decodificar(codificado: str) -> str:
    """Decodifica um texto em URL encoding."""
    return urllib.parse.unquote(codificado)
