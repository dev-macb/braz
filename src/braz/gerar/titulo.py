from secrets import SystemRandom

from braz.shared.digit import (
    TITULO_WEIGHTS_1,
    TITULO_WEIGHTS_2,
    calcular_digito_verificador,
)

_rand = SystemRandom()


def titulo(formatar: bool = False) -> str:
    """Gera um Titulo de Eleitor valido.

    Args:
        formatar: Se True, retorna no formato 0000 0000 0000 00.

    Returns:
        str: Titulo com 12 digitos + 2 DV.
    """
    base = [_rand.randint(0, 9) for _ in range(12)]
    part1 = base[:8]
    part2 = base[8:]

    d1 = calcular_digito_verificador(part1, TITULO_WEIGHTS_1)
    d2 = calcular_digito_verificador([*part2, d1], TITULO_WEIGHTS_2)

    if d1 > 9:
        d1 = 0
    if d2 > 9:
        d2 = 0

    digitos = [*base, d1, d2]
    valor = "".join(str(x) for x in digitos)
    if formatar:
        return f"{valor[:4]} {valor[4:8]} {valor[8:12]} {valor[12:]}"
    return valor
