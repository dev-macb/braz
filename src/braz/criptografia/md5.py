import hashlib


def md5(texto: str) -> str:
    """Gera hash MD5 de um texto."""
    return hashlib.md5(texto.encode()).hexdigest()  # noqa: S324
