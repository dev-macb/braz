from secrets import SystemRandom

_rand = SystemRandom()


def telefone() -> str:
    """Gera um numero de telefone brasileiro.

    Returns:
        str: Telefone no formato (DD) 0000-0000.
    """
    ddd = _rand.randint(11, 99)
    prefix = _rand.randint(1000, 9999)
    suffix = _rand.randint(1000, 9999)
    return f"({ddd}) {prefix}-{suffix}"
