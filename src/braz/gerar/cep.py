from secrets import SystemRandom

_rand = SystemRandom()


def cep(formatar: bool = False) -> str:
    """Gera um CEP valido.

    Args:
        formatar: Se True, retorna no formato 00000-000.

    Returns:
        str: CEP com 8 digitos.
    """
    digitos = [_rand.randint(0, 9) for _ in range(8)]
    valor = "".join(str(x) for x in digitos)
    if formatar:
        return f"{valor[:5]}-{valor[5:]}"
    return valor
