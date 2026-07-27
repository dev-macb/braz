def cifrar(texto: str) -> str:
    """Converte texto para representacao binaria (8 bits por caractere)."""
    return " ".join(format(ord(c), "08b") for c in texto)


def decifrar(binario: str) -> str:
    """Converte representacao binaria de volta para texto.

    Args:
        binario: Sequencia de bytes em binario separados por espaco.

    Returns:
        str: Texto decodificado.
    """
    caracteres = [chr(int(b, 2)) for b in binario.split()]
    return "".join(caracteres)
