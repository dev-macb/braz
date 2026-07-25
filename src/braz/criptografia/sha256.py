import hashlib


def sha256(texto: str) -> str:
    """Gera hash SHA-256 de um texto."""
    return hashlib.sha256(texto.encode()).hexdigest()
