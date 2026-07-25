import hashlib


def sha1(texto: str) -> str:
    """Gera hash SHA-1 de um texto."""
    return hashlib.sha1(texto.encode()).hexdigest()  # noqa: S324
