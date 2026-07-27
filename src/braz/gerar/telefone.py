from secrets import SystemRandom

_rand = SystemRandom()


def telefone(formatar: bool = False) -> str:
    """Gera um numero de telefone brasileiro.

    Args:
        formatar: Se True, retorna no formato (DD) 0000-0000.

    Returns:
        str: Telefone com 10 digitos.
    """
    ddd = _rand.randint(11, 99)
    prefixo = _rand.randint(1000, 9999)
    sufixo = _rand.randint(1000, 9999)
    valor = f"{ddd}{prefixo}{sufixo}"
    if formatar:
        return f"({ddd}) {prefixo}-{sufixo}"
    return valor
