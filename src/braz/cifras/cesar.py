def _shift(texto: str, shift: int, direction: int) -> str:
    result = []
    for c in texto:
        if "A" <= c <= "Z":
            result.append(chr((ord(c) - 65 + shift * direction) % 26 + 65))
        elif "a" <= c <= "z":
            result.append(chr((ord(c) - 97 + shift * direction) % 26 + 97))
        else:
            result.append(c)
    return "".join(result)


def encrypt(texto: str, shift: int) -> str:
    """Aplica a cifra de Cesar em um texto.

    Args:
        texto: Texto original.
        shift: Deslocamento (numero de posicoes).

    Returns:
        str: Texto cifrado.
    """
    return _shift(texto, shift, 1)


def decrypt(texto: str, shift: int) -> str:
    """Decifra um texto cifrado com Cesar.

    Args:
        texto: Texto cifrado.
        shift: Deslocamento utilizado na cifragem.

    Returns:
        str: Texto decifrado.
    """
    return _shift(texto, shift, -1)
