import hashlib


def sha3_224(texto: str) -> str:
    """Gera hash SHA3-224 de um texto."""
    return hashlib.sha3_224(texto.encode()).hexdigest()


def sha3_256(texto: str) -> str:
    """Gera hash SHA3-256 de um texto."""
    return hashlib.sha3_256(texto.encode()).hexdigest()


def sha3_384(texto: str) -> str:
    """Gera hash SHA3-384 de um texto."""
    return hashlib.sha3_384(texto.encode()).hexdigest()


def sha3_512(texto: str) -> str:
    """Gera hash SHA3-512 de um texto."""
    return hashlib.sha3_512(texto.encode()).hexdigest()
