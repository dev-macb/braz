from secrets import SystemRandom

from braz.shared.digit import CNPJ_WEIGHTS_1, CNPJ_WEIGHTS_2, compute_check_digit

_rand = SystemRandom()


def cnpj() -> str:
    """Gera um CNPJ valido.

    Returns:
        str: CNPJ com 14 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(12)]
    d1 = compute_check_digit(base, CNPJ_WEIGHTS_1)
    d2 = compute_check_digit([*base, d1], CNPJ_WEIGHTS_2)
    digits = [*base, d1, d2]
    return "".join(str(d) for d in digits)
