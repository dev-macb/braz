from secrets import SystemRandom

from braz.shared.digit import TITULO_WEIGHTS_1, TITULO_WEIGHTS_2, compute_check_digit

_rand = SystemRandom()


def titulo() -> str:
    """Gera um Titulo de Eleitor valido.

    Returns:
        str: Titulo com 12 digitos + 2 DV.
    """
    base = [_rand.randint(0, 9) for _ in range(12)]
    part1 = base[:8]
    part2 = base[8:]

    d1 = compute_check_digit(part1, TITULO_WEIGHTS_1)
    d2 = compute_check_digit([*part2, d1], TITULO_WEIGHTS_2)

    if d1 > 9:
        d1 = 0
    if d2 > 9:
        d2 = 0

    digits = [*base, d1, d2]
    return "".join(str(x) for x in digits)
