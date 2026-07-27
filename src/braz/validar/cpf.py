from braz.shared.digit import CPF_WEIGHTS_1, CPF_WEIGHTS_2, calcular_digito_verificador
from braz.shared.helpers import todos_mesmo_digito, apenas_digitos


def cpf(numero: str) -> bool:
    """Valida um CPF.

    Args:
        numero: CPF com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digitos = apenas_digitos(numero)
    if len(digitos) != 11 or todos_mesmo_digito(digitos):
        return False
    numeros = [int(d) for d in digitos]
    d1 = calcular_digito_verificador(numeros[:9], CPF_WEIGHTS_1)
    if d1 != numeros[9]:
        return False
    d2 = calcular_digito_verificador(numeros[:10], CPF_WEIGHTS_2)
    return d2 == numeros[10]
