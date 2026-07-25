from secrets import SystemRandom

from braz.shared.digit import RENAVAM_WEIGHTS

_rand = SystemRandom()


def renavam() -> str:
    """Gera um RENAVAM valido.

    Returns:
        str: RENAVAM com 10 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(9)]
    total = sum(d * w for d, w in zip(base, RENAVAM_WEIGHTS))
    remainder = total % 11
    d = 0 if remainder >= 10 else remainder
    digits = [*base, d]
    return "".join(str(x) for x in digits)
