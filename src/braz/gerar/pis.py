from secrets import SystemRandom

from braz.shared.digit import PIS_WEIGHTS, compute_check_digit

_rand = SystemRandom()


def pis() -> str:
    """Gera um PIS/PASEP valido.

    Returns:
        str: PIS com 11 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(10)]
    d = compute_check_digit(base, PIS_WEIGHTS)
    digits = [*base, d]
    return "".join(str(x) for x in digits)
