import re
import unicodedata


def remove_accents(texto: str) -> str:
    """Remove acentos de uma string.

    Exemplo: "cafe" -> "cafe"
    """
    nfkd = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def remove_spaces(texto: str) -> str:
    """Remove todos os espacos de uma string."""
    return texto.replace(" ", "")


def remove_special_chars(texto: str) -> str:
    """Remove caracteres especiais mantendo letras, numeros e espacos."""
    return re.sub(r"[^a-zA-Z0-9\s]", "", texto)


def only_digits(texto: str) -> str:
    """Mantem apenas os digitos numericos."""
    return re.sub(r"\D", "", texto)


def only_letters(texto: str) -> str:
    """Mantem apenas letras (a-z, A-Z)."""
    return re.sub(r"[^a-zA-Z]", "", texto)
