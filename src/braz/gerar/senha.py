from secrets import SystemRandom

_rand = SystemRandom()

ASCII = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"


def senha(comprimento: int = 16, formatar: bool = False) -> str:
    """Gera uma senha aleatoria segura.

    Args:
        comprimento: Comprimento da senha (padrao 16).
        formatar: Ignorado (senha nao possui formatacao).

    Returns:
        str: Senha aleatoria.
    """
    return "".join(_rand.choice(ASCII) for _ in range(comprimento))
