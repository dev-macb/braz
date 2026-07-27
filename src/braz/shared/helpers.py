import re


def apenas_digitos(texto: str) -> str:
    """Remove todos os caracteres nao numericos de uma string."""
    return re.sub(r"\D", "", texto)


def todos_mesmo_digito(texto: str) -> bool:
    """Verifica se todos os caracteres da string sao iguais."""
    return len(set(texto)) == 1
