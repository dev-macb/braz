from secrets import SystemRandom

_rand = SystemRandom()


def placa(formatar: bool = False) -> str:
    """Gera uma placa de veiculo brasileira (formato AAA-0000).

    Args:
        formatar: Se True, retorna no formato AAA-0000.

    Returns:
        str: Placa com 7 caracteres.
    """
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = "".join(_rand.choice(alfabeto) for _ in range(3))
    digitos = "".join(str(_rand.randint(0, 9)) for _ in range(4))
    valor = f"{letras}{digitos}"
    if formatar:
        return f"{letras}-{digitos}"
    return valor
