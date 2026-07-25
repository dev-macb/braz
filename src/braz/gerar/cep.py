from secrets import SystemRandom

_rand = SystemRandom()


def cep() -> str:
    """Gera um CEP valido.

    Returns:
        str: CEP no formato 00000-000.
    """
    digits = [_rand.randint(0, 9) for _ in range(8)]
    d = "".join(str(x) for x in digits)
    return d[:5] + "-" + d[5:]
