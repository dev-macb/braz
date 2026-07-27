from braz.shared.digit import CNPJ_WEIGHTS_1, CNPJ_WEIGHTS_2, calcular_digito_verificador
from braz.shared.helpers import todos_mesmo_digito, apenas_digitos


def cnpj(numero: str) -> bool:
    """Valida um CNPJ.

    Args:
        numero: CNPJ com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digitos = apenas_digitos(numero)
    if len(digitos) != 14 or todos_mesmo_digito(digitos):
        return False
    numeros = [int(d) for d in digitos]
    d1 = calcular_digito_verificador(numeros[:12], CNPJ_WEIGHTS_1)
    if d1 != numeros[12]:
        return False
    d2 = calcular_digito_verificador(numeros[:13], CNPJ_WEIGHTS_2)
    return d2 == numeros[13]
