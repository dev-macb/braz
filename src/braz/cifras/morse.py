_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

_REVERSO = {v: k for k, v in _MORSE.items()}


def cifrar(texto: str) -> str:
    """Converte texto para codigo Morse.

    Palavras separadas por " / ".
    """
    palavras = texto.upper().split()
    return " / ".join(" ".join(_MORSE.get(c, c) for c in w) for w in palavras)


def decifrar(codigo_morse: str) -> str:
    """Converte codigo Morse de volta para texto."""
    palavras = codigo_morse.split(" / ")
    resultado = []
    for palavra in palavras:
        caracteres = palavra.split()
        resultado.append("".join(_REVERSO.get(c, c) for c in caracteres))
    return " ".join(resultado)
