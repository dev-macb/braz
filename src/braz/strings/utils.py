import re
import unicodedata


def slug(texto: str) -> str:
    """Converte texto para slug URL-friendly.

    Exemplo: "Ola Mundo!" -> "ola-mundo"
    """
    nfkd = unicodedata.normalize("NFKD", texto)
    texto_limpo = "".join(c for c in nfkd if not unicodedata.combining(c))
    texto_limpo = re.sub(r"[^a-zA-Z0-9\s-]", "", texto_limpo)
    texto_limpo = re.sub(r"[\s]+", "-", texto_limpo.strip())
    return texto_limpo.lower()


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


def truncate(texto: str, comprimento: int, sufixo: str = "...") -> str:
    """Trunca um texto para um tamanho maximo.

    Args:
        texto: Texto original.
        comprimento: Tamanho maximo.
        sufixo: Sufixo adicionado ao final (padrao "...").

    Returns:
        str: Texto truncado.
    """
    if len(texto) <= comprimento:
        return texto
    return texto[:comprimento].rstrip() + sufixo


def pad(texto: str, largura: int, caractere: str = " ") -> str:
    """Centraliza um texto preenchendo com um caractere.

    Args:
        texto: Texto original.
        largura: Largura total.
        caractere: Caractere de preenchimento (padrao espaco).

    Returns:
        str: Texto centralizado.
    """
    return texto.center(largura, caractere)


def replace(texto: str, antigo: str, novo: str) -> str:
    """Substitui ocorrencias de um texto por outro."""
    return texto.replace(antigo, novo)
