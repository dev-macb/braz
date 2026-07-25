import urllib.parse


def encode(texto: str) -> str:
    """Codifica um texto para URL encoding."""
    return urllib.parse.quote(texto)


def decode(codificado: str) -> str:
    """Decodifica um texto em URL encoding."""
    return urllib.parse.unquote(codificado)
