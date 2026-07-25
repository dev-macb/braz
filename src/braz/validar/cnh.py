from braz.shared.digit import CNH_WEIGHTS_1, CNH_WEIGHTS_2, compute_check_digit
from braz.shared.helpers import only_digits


def cnh(numero: str) -> bool:
    """Valida uma CNH.

    Args:
        numero: CNH com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digits = only_digits(numero)
    if len(digits) != 11:
        return False
    nums = [int(d) for d in digits]
    d1 = compute_check_digit(nums[:9], CNH_WEIGHTS_1)
    if d1 != nums[9]:
        return False
    d2 = compute_check_digit(nums[:10], CNH_WEIGHTS_2)
    return d2 == nums[10]
