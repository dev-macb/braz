import bcrypt as _bcrypt


def bcrypt(texto: str) -> str:
    """Gera hash bcrypt de um texto.

    Args:
        texto: Texto para hashing.

    Returns:
        str: Hash bcrypt.
    """
    return _bcrypt.hashpw(texto.encode(), _bcrypt.gensalt()).decode()


def verificar_bcrypt(texto: str, texto_hash: str) -> bool:
    """Verifica se um texto corresponde a um hash bcrypt.

    Args:
        texto: Texto a verificar.
        texto_hash: Hash bcrypt armazenado.

    Returns:
        bool: True se corresponder, False caso contrario.
    """
    return _bcrypt.checkpw(texto.encode(), texto_hash.encode())
