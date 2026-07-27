def _deslocamento(texto: str, deslocamento: int, direcao: int) -> str:
    resultado = []
    for c in texto:
        if "A" <= c <= "Z":
            resultado.append(chr((ord(c) - 65 + deslocamento * direcao) % 26 + 65))
        elif "a" <= c <= "z":
            resultado.append(chr((ord(c) - 97 + deslocamento * direcao) % 26 + 97))
        else:
            resultado.append(c)
    return "".join(resultado)


def cifrar(texto: str, deslocamento: int) -> str:
    """Aplica a cifra de Cesar em um texto.

    Args:
        texto: Texto original.
        deslocamento: Deslocamento (numero de posicoes).

    Returns:
        str: Texto cifrado.
    """
    return _deslocamento(texto, deslocamento, 1)


def decifrar(texto: str, deslocamento: int) -> str:
    """Decifra um texto cifrado com Cesar.

    Args:
        texto: Texto cifrado.
        deslocamento: Deslocamento utilizado na cifragem.

    Returns:
        str: Texto decifrado.
    """
    return _deslocamento(texto, deslocamento, -1)
