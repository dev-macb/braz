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

_REVERSE = {v: k for k, v in _MORSE.items()}


def encrypt(texto: str) -> str:
    """Converte texto para codigo Morse.

    Palavras separadas por " / ".
    """
    words = texto.upper().split()
    return " / ".join(" ".join(_MORSE.get(c, c) for c in w) for w in words)


def decrypt(morse: str) -> str:
    """Converte codigo Morse de volta para texto."""
    words = morse.split(" / ")
    result = []
    for word in words:
        chars = word.split()
        result.append("".join(_REVERSE.get(c, c) for c in chars))
    return " ".join(result)
