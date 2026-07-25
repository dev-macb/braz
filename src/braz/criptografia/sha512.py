import hashlib


def sha512(texto: str) -> str:
    """Gera hash SHA-512 de um texto."""
    return hashlib.sha512(texto.encode()).hexdigest()
