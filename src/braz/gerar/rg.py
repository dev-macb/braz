from secrets import SystemRandom

_rand = SystemRandom()


def rg() -> str:
    """Gera um RG valido (formato SP).

    Returns:
        str: RG com 9 caracteres (8 digitos + 1 digito verificador).
    """
    digits = [_rand.randint(0, 9) for _ in range(8)]
    total = sum(d * w for d, w in zip(digits, range(2, 10)))
    remainder = total % 11
    if remainder == 10:
        d = "X"
    else:
        d = str(remainder)
    return "".join(str(x) for x in digits) + d
