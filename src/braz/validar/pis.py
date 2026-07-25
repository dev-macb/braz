from braz.shared.digit import PIS_WEIGHTS, compute_check_digit
from braz.shared.helpers import all_same_digit, only_digits


def pis(numero: str) -> bool:
    """Valida um PIS/PASEP.

    Args:
        numero: PIS com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digits = only_digits(numero)
    if len(digits) != 11 or all_same_digit(digits):
        return False
    nums = [int(d) for d in digits]
    d = compute_check_digit(nums[:10], PIS_WEIGHTS)
    return d == nums[10]
