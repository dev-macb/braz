from braz.shared.digit import PIS_WEIGHTS, calcular_digito_verificador
from braz.shared.helpers import apenas_digitos, todos_mesmo_digito


def pis(numero: str) -> bool:
    """Valida um PIS/PASEP.

    Args:
        numero: PIS com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digitos = apenas_digitos(numero)
    if len(digitos) != 11 or todos_mesmo_digito(digitos):
        return False
    numeros = [int(d) for d in digitos]
    d = calcular_digito_verificador(numeros[:10], PIS_WEIGHTS)
    return d == numeros[10]
