import re


def only_digits(text: str) -> str:
    """Remove todos os caracteres nao numericos de uma string."""
    return re.sub(r"\D", "", text)


def all_same_digit(text: str) -> bool:
    """Verifica se todos os caracteres da string sao iguais."""
    return len(set(text)) == 1
