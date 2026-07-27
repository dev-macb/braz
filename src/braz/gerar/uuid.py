import uuid


def uuid4(formatar: bool = False) -> str:
    """Gera um UUID versao 4.

    Args:
        formatar: Ignorado (UUID nao possui formatacao).

    Returns:
        str: UUID v4.
    """
    return str(uuid.uuid4())
