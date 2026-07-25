import re


def cep(numero: str) -> bool:
    """Valida um CEP.

    Args:
        numero: CEP no formato 00000-000 ou 00000000.

    Returns:
        bool: True se valido, False caso contrario.
    """
    return bool(re.fullmatch(r"\d{5}-?\d{3}", numero))
