import hashlib


def sha384(texto: str) -> str:
    """Gera hash SHA-384 de um texto."""
    return hashlib.sha384(texto.encode()).hexdigest()
