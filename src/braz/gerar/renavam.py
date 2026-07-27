from secrets import SystemRandom

from braz.shared.digit import RENAVAM_WEIGHTS

_rand = SystemRandom()


def renavam(formatar: bool = False) -> str:
    """Gera um RENAVAM valido.

    Args:
        formatar: Se True, retorna no formato 0000.000000-0.

    Returns:
        str: RENAVAM com 10 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(9)]
    total = sum(d * w for d, w in zip(base, RENAVAM_WEIGHTS))
    resto = total % 11
    d = 0 if resto >= 10 else resto
    digitos = [*base, d]
    valor = "".join(str(x) for x in digitos)
    if formatar:
        return f"{valor[:4]}.{valor[4:9]}-{valor[9:]}"
    return valor
