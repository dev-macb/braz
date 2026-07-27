from secrets import SystemRandom

from braz.shared.digit import CNPJ_WEIGHTS_1, CNPJ_WEIGHTS_2, calcular_digito_verificador

_rand = SystemRandom()


def cnpj(formatar: bool = False) -> str:
    """Gera um CNPJ valido.

    Args:
        formatar: Se True, retorna no formato 00.000.000/0000-00.

    Returns:
        str: CNPJ com 14 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(12)]
    d1 = calcular_digito_verificador(base, CNPJ_WEIGHTS_1)
    d2 = calcular_digito_verificador([*base, d1], CNPJ_WEIGHTS_2)
    digitos = [*base, d1, d2]
    valor = "".join(str(d) for d in digitos)
    if formatar:
        return f"{valor[:2]}.{valor[2:5]}.{valor[5:8]}/{valor[8:12]}-{valor[12:]}"
    return valor
