def _vigenere(texto: str, chave: str, direcao: int) -> str:
    resultado = []
    indice_chave = 0
    for c in texto:
        if "A" <= c <= "Z":
            deslocamento = ord(chave[indice_chave % len(chave)].upper()) - 65
            resultado.append(chr((ord(c) - 65 + deslocamento * direcao) % 26 + 65))
            indice_chave += 1
        elif "a" <= c <= "z":
            deslocamento = ord(chave[indice_chave % len(chave)].upper()) - 65
            resultado.append(chr((ord(c) - 97 + deslocamento * direcao) % 26 + 97))
            indice_chave += 1
        else:
            resultado.append(c)
    return "".join(resultado)


def cifrar(texto: str, chave: str) -> str:
    """Aplica a cifra de Vigenere.

    Args:
        texto: Texto original.
        chave: Palavra-chave para cifragem.

    Returns:
        str: Texto cifrado.
    """
    return _vigenere(texto, chave, 1)


def decifrar(texto: str, chave: str) -> str:
    """Decifra um texto cifrado com Vigenere.

    Args:
        texto: Texto cifrado.
        chave: Palavra-chave utilizada na cifragem.

    Returns:
        str: Texto decifrado.
    """
    return _vigenere(texto, chave, -1)
