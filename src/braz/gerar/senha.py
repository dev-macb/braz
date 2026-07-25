from secrets import SystemRandom

_rand = SystemRandom()

ASCII = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"


def senha(length: int = 16) -> str:
    """Gera uma senha aleatoria segura.

    Args:
        length: Comprimento da senha (padrao 16).

    Returns:
        str: Senha aleatoria.
    """
    return "".join(_rand.choice(ASCII) for _ in range(length))
