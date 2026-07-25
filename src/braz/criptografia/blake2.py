import hashlib


def blake2b(texto: str) -> str:
    """Gera hash BLAKE2b de um texto."""
    return hashlib.blake2b(texto.encode()).hexdigest()


def blake2s(texto: str) -> str:
    """Gera hash BLAKE2s de um texto."""
    return hashlib.blake2s(texto.encode()).hexdigest()
