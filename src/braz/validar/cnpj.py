from braz.shared.digit import CNPJ_WEIGHTS_1, CNPJ_WEIGHTS_2, compute_check_digit
from braz.shared.helpers import all_same_digit, only_digits


def cnpj(numero: str) -> bool:
    """Valida um CNPJ.

    Args:
        numero: CNPJ com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digits = only_digits(numero)
    if len(digits) != 14 or all_same_digit(digits):
        return False
    nums = [int(d) for d in digits]
    d1 = compute_check_digit(nums[:12], CNPJ_WEIGHTS_1)
    if d1 != nums[12]:
        return False
    d2 = compute_check_digit(nums[:13], CNPJ_WEIGHTS_2)
    return d2 == nums[13]
