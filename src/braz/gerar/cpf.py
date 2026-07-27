from secrets import SystemRandom

from braz.shared.digit import CPF_WEIGHTS_1, CPF_WEIGHTS_2, calcular_digito_verificador

_rand = SystemRandom()


def cpf(formatar: bool = False) -> str:
    """Gera um CPF valido.

    Args:
        formatar: Se True, retorna no formato 000.000.000-00.

    Returns:
        str: CPF com 11 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(9)]
    d1 = calcular_digito_verificador(base, CPF_WEIGHTS_1)
    d2 = calcular_digito_verificador([*base, d1], CPF_WEIGHTS_2)
    digitos = [*base, d1, d2]
    valor = "".join(str(d) for d in digitos)
    if formatar:
        return f"{valor[:3]}.{valor[3:6]}.{valor[6:9]}-{valor[9:]}"
    return valor
