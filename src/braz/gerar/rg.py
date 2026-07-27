from secrets import SystemRandom

_rand = SystemRandom()


def rg(formatar: bool = False) -> str:
    """Gera um RG valido (formato SP).

    Args:
        formatar: Se True, retorna no formato 00.000.000-X.

    Returns:
        str: RG com 9 caracteres (8 digitos + 1 digito verificador).
    """
    digitos = [_rand.randint(0, 9) for _ in range(8)]
    total = sum(d * w for d, w in zip(digitos, range(2, 10)))
    resto = total % 11
    if resto == 10:
        d = "X"
    else:
        d = str(resto)
    valor = "".join(str(x) for x in digitos) + d
    if formatar:
        return f"{valor[:2]}.{valor[2:5]}.{valor[5:8]}-{valor[8:]}"
    return valor
