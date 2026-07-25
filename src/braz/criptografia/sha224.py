import hashlib


def sha224(texto: str) -> str:
    """Gera hash SHA-224 de um texto."""
    return hashlib.sha224(texto.encode()).hexdigest()
