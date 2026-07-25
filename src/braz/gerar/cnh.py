from secrets import SystemRandom

from braz.shared.digit import CNH_WEIGHTS_1, CNH_WEIGHTS_2, compute_check_digit

_rand = SystemRandom()


def cnh() -> str:
    """Gera uma CNH valida.

    Returns:
        str: CNH com 11 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(9)]
    d1 = compute_check_digit(base, CNH_WEIGHTS_1)
    d2 = compute_check_digit([*base, d1], CNH_WEIGHTS_2)
    digits = [*base, d1, d2]
    return "".join(str(d) for d in digits)
