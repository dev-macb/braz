from braz.shared.digit import compute_check_digit
from braz.shared.helpers import all_same_digit, only_digits


def test_only_digits():
    assert only_digits("abc123def456") == "123456"


def test_only_digits_vazio():
    assert only_digits("") == ""


def test_only_digits_sem_numeros():
    assert only_digits("abc") == ""


def test_all_same_digit_true():
    assert all_same_digit("11111")


def test_all_same_digit_false():
    assert not all_same_digit("12345")


def test_all_same_digit_vazio():
    assert not all_same_digit("")


def test_compute_check_digit():
    base = [0, 1, 1, 2, 3, 4, 5, 6, 7]
    weights = list(range(10, 1, -1))
    result = compute_check_digit(base, weights)
    assert isinstance(result, int)
    assert 0 <= result <= 9


def test_compute_check_digit_resto_0():
    base = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    weights = list(range(10, 1, -1))
    assert compute_check_digit(base, weights) == 0
