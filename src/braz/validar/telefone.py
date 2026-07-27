import re

from braz.shared.helpers import apenas_digitos


def telefone(numero: str) -> bool:
    """Valida um numero de telefone brasileiro.

    Args:
        numero: Telefone com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digitos = apenas_digitos(numero)
    if len(digitos) not in (10, 11):
        return False
    return bool(re.fullmatch(r"\d{10,11}", digitos))
