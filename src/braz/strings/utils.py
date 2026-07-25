import re
import unicodedata


def slug(texto: str) -> str:
    """Converte texto para slug URL-friendly.

    Exemplo: "Ola Mundo!" -> "ola-mundo"
    """
    nfkd = unicodedata.normalize("NFKD", texto)
    text = "".join(c for c in nfkd if not unicodedata.combining(c))
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text.strip())
    return text.lower()


def reverse(texto: str) -> str:
    """Inverte uma string."""
    return texto[::-1]


def count_chars(texto: str) -> int:
    """Conta o numero de caracteres."""
    return len(texto)


def count_words(texto: str) -> int:
    """Conta o numero de palavras."""
    return len(texto.split())


def repeat(texto: str, vezes: int) -> str:
    """Repete um texto N vezes."""
    return texto * vezes


def truncate(texto: str, length: int, suffix: str = "...") -> str:
    """Trunca um texto para um tamanho maximo.

    Args:
        texto: Texto original.
        length: Tamanho maximo.
        suffix: Sufixo adicionado ao final (padrao "...").

    Returns:
        str: Texto truncado.
    """
    if len(texto) <= length:
        return texto
    return texto[:length].rstrip() + suffix


def pad(texto: str, width: int, char: str = " ") -> str:
    """Centraliza um texto preenchendo com um caractere.

    Args:
        texto: Texto original.
        width: Largura total.
        char: Caractere de preenchimento (padrao espaco).

    Returns:
        str: Texto centralizado.
    """
    return texto.center(width, char)


def replace(texto: str, old: str, new: str) -> str:
    """Substitui ocorrencias de um texto por outro."""
    return texto.replace(old, new)
