from braz.shared.digit import CNH_WEIGHTS_1, CNH_WEIGHTS_2, calcular_digito_verificador
from braz.shared.helpers import apenas_digitos


def cnh(numero: str) -> bool:
    """Valida uma CNH.

    Args:
        numero: CNH com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digitos = apenas_digitos(numero)
    if len(digitos) != 11:
        return False
    numeros = [int(d) for d in digitos]
    d1 = calcular_digito_verificador(numeros[:9], CNH_WEIGHTS_1)
    if d1 != numeros[9]:
        return False
    d2 = calcular_digito_verificador(numeros[:10], CNH_WEIGHTS_2)
    return d2 == numeros[10]
