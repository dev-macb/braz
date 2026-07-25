from braz.shared.helpers import only_digits


def cpf(numero: str) -> str:
    """Formata CPF: 000.000.000-00."""
    d = only_digits(numero)
    return f"{d[:3]}.{d[3:6]}.{d[6:9]}-{d[9:]}"


def cnpj(numero: str) -> str:
    """Formata CNPJ: 00.000.000/0000-00."""
    d = only_digits(numero)
    return f"{d[:2]}.{d[2:5]}.{d[5:8]}/{d[8:12]}-{d[12:]}"


def rg(numero: str) -> str:
    """Formata RG: 00.000.000-X."""
    d = only_digits(numero)
    suffix = numero[-1] if not numero[-1].isdigit() else ""
    return f"{d[:2]}.{d[2:5]}.{d[5:8]}-{d[8:]}{suffix}"


def pis(numero: str) -> str:
    """Formata PIS: 000.00000.00-0."""
    d = only_digits(numero)
    return f"{d[:3]}.{d[3:8]}.{d[8:10]}-{d[10:]}"


def cep(numero: str) -> str:
    """Formata CEP: 00000-000."""
    d = only_digits(numero)
    return f"{d[:5]}-{d[5:]}"


def telefone(numero: str) -> str:
    """Formata telefone: (00) 0000-0000 ou (00) 00000-0000."""
    d = only_digits(numero)
    if len(d) == 10:
        return f"({d[:2]}) {d[2:6]}-{d[6:]}"
    return f"({d[:2]}) {d[2:7]}-{d[7:]}"


def titulo(numero: str) -> str:
    """Formata Titulo de Eleitor: 0000 0000 0000."""
    d = only_digits(numero)
    return f"{d[:4]} {d[4:8]} {d[8:12]} {d[12:]}"


def placa(numero: str) -> str:
    """Placa ja vem formatada."""
    return numero


def cnh(numero: str) -> str:
    """CNH sem formato padrao definido."""
    return numero


def renavam(numero: str) -> str:
    """RENAVAM sem formato padrao definido."""
    return numero


def uuid(numero: str) -> str:
    """UUID ja vem formatado."""
    return numero


def senha(numero: str) -> str:
    """Senha sem formatacao."""
    return numero
