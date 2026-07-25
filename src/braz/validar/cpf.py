from braz.shared.digit import CPF_WEIGHTS_1, CPF_WEIGHTS_2, compute_check_digit
from braz.shared.helpers import all_same_digit, only_digits


def cpf(numero: str) -> bool:
    """Valida um CPF.

    Args:
        numero: CPF com ou sem mascara.

    Returns:
        bool: True se valido, False caso contrario.
    """
    digits = only_digits(numero)
    if len(digits) != 11 or all_same_digit(digits):
        return False
    nums = [int(d) for d in digits]
    d1 = compute_check_digit(nums[:9], CPF_WEIGHTS_1)
    if d1 != nums[9]:
        return False
    d2 = compute_check_digit(nums[:10], CPF_WEIGHTS_2)
    return d2 == nums[10]
