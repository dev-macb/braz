from secrets import SystemRandom

from braz.shared.digit import CPF_WEIGHTS_1, CPF_WEIGHTS_2, compute_check_digit

_rand = SystemRandom()


def cpf() -> str:
    """Gera um CPF valido.

    Returns:
        str: CPF com 11 digitos.
    """
    base = [_rand.randint(0, 9) for _ in range(9)]
    d1 = compute_check_digit(base, CPF_WEIGHTS_1)
    d2 = compute_check_digit([*base, d1], CPF_WEIGHTS_2)
    digits = [*base, d1, d2]
    return "".join(str(d) for d in digits)
