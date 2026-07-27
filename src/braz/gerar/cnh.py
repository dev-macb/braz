from secrets import SystemRandom

from braz.shared.digit import CNH_WEIGHTS_1, CNH_WEIGHTS_2, calcular_digito_verificador

_rand = SystemRandom()


def cnh(formatar: bool = False) -> str:
    """Gera uma CNH valida.

    Args:
        formatar: Se True, retorna no formato 000000000-00.

    Returns:
        str: CNH com 11 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(9)]
    d1 = calcular_digito_verificador(base, CNH_WEIGHTS_1)
    d2 = calcular_digito_verificador([*base, d1], CNH_WEIGHTS_2)
    digitos = [*base, d1, d2]
    valor = "".join(str(d) for d in digitos)
    if formatar:
        return f"{valor[:9]}-{valor[9:]}"
    return valor
