from secrets import SystemRandom

from braz.shared.digit import PIS_WEIGHTS, calcular_digito_verificador

_rand = SystemRandom()


def pis(formatar: bool = False) -> str:
    """Gera um PIS/PASEP valido.

    Args:
        formatar: Se True, retorna no formato 000.00000.00-0.

    Returns:
        str: PIS com 11 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(10)]
    d = calcular_digito_verificador(base, PIS_WEIGHTS)
    digitos = [*base, d]
    valor = "".join(str(x) for x in digitos)
    if formatar:
        return f"{valor[:3]}.{valor[3:8]}.{valor[8:10]}-{valor[10:]}"
    return valor
