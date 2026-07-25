import uuid


def uuid4() -> str:
    """Gera um UUID versao 4.

    Returns:
        str: UUID v4.
    """
    return str(uuid.uuid4())
