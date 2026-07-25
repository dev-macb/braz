from braz.shared.helpers import all_same_digit


def _clean_rg(numero: str) -> str:
    return "".join(c for c in numero if c.isdigit() or c.upper() == "X")


def rg(numero: str) -> bool:
    """Valida um RG.

    Args:
        numero: RG com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    cleaned = _clean_rg(numero)
    if len(cleaned) != 9:
        return False
    if cleaned[-1] == "X" and all_same_digit(cleaned[:-1]):
        return False
    if cleaned[-1] != "X" and all_same_digit(cleaned):
        return False
    nums = [int(d) for d in cleaned[:8] if d.isdigit()]
    if len(nums) != 8:
        return False
    total = sum(d * w for d, w in zip(nums, range(2, 10)))
    remainder = total % 11
    expected = "X" if remainder == 10 else str(remainder)
    return cleaned[-1].upper() == expected
