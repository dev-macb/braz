from braz.shared.helpers import todos_mesmo_digito


def _clean_rg(numero: str) -> str:
    return "".join(c for c in numero if c.isdigit() or c.upper() == "X")


def rg(numero: str) -> bool:
    """Valida um RG.

    Args:
        numero: RG com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    limpo = _clean_rg(numero)
    if len(limpo) != 9:
        return False
    if limpo[-1] == "X" and todos_mesmo_digito(limpo[:-1]):
        return False
    if limpo[-1] != "X" and todos_mesmo_digito(limpo):
        return False
    numeros = [int(d) for d in limpo[:8] if d.isdigit()]
    if len(numeros) != 8:
        return False
    total = sum(d * w for d, w in zip(numeros, range(2, 10)))
    resto = total % 11
    esperado = "X" if resto == 10 else str(resto)
    return limpo[-1].upper() == esperado
