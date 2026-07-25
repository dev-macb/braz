import re


def email(endereco: str) -> bool:
    """Valida um endereco de email.

    Args:
        endereco: Email para validacao.

    Returns:
        bool: True se valido, False caso contrario.
    """
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", endereco))
