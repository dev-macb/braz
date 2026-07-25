from secrets import SystemRandom

_rand = SystemRandom()


def placa() -> str:
    """Gera uma placa de veiculo brasileira (formato AAA-0000).

    Returns:
        str: Placa no formato AAA-0000.
    """
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = "".join(_rand.choice(letters) for _ in range(3))
    digitos = "".join(str(_rand.randint(0, 9)) for _ in range(4))
    return f"{letras}-{digitos}"
