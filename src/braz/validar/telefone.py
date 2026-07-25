import re

from braz.shared.helpers import only_digits


def telefone(numero: str) -> bool:
    """Valida um numero de telefone brasileiro.

    Args:
        numero: Telefone com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digits = only_digits(numero)
    if len(digits) not in (10, 11):
        return False
    return bool(re.fullmatch(r"\d{10,11}", digits))
