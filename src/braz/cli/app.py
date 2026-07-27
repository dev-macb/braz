import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="braz",
        description="CLI para geracao, validacao e transformacao de dados",
    )
    parser.add_argument(
        "-v", "--versao", action="store_true", help="Exibe a versao da CLI"
    )
    subanalisadores = parser.add_subparsers(dest="modulo")

    # gerar
    p = subanalisadores.add_parser("gerar", help="Gera dados validos")
    p.add_argument("-f", "--formatar", action="store_true", help="Exibe formatado")
    p.add_argument("--cpf", action="store_true", help="Gera CPF")
    p.add_argument("--cnpj", action="store_true", help="Gera CNPJ")
    p.add_argument("--rg", action="store_true", help="Gera RG")
    p.add_argument("--cnh", action="store_true", help="Gera CNH")
    p.add_argument("--pis", action="store_true", help="Gera PIS/PASEP")
    p.add_argument("--titulo", action="store_true", help="Gera Titulo de Eleitor")
    p.add_argument("--renavam", action="store_true", help="Gera RENAVAM")
    p.add_argument("--cep", action="store_true", help="Gera CEP")
    p.add_argument("--telefone", action="store_true", help="Gera Telefone")
    p.add_argument("--placa", action="store_true", help="Gera Placa")
    p.add_argument("--uuid", action="store_true", help="Gera UUID")
    p.add_argument(
        "--senha", nargs="?", const=16, type=int, help="Gera senha (opcional: tamanho)"
    )

    # validar
    p = subanalisadores.add_parser("validar", help="Valida informacoes")
    for documento in ["cpf", "cnpj", "rg", "cnh", "pis", "cep", "email", "telefone"]:
        p.add_argument(
            f"--{documento}", nargs=1, metavar="VALOR",
            help=f"Valida {documento.upper()}",
        )

    # cifrar
    p = subanalisadores.add_parser("cifrar", help="Cifra textos (cifras classicas)")
    p.add_argument(
        "--cesar", nargs=2, metavar=("DESLOCAMENTO", "TEXTO"), help="Cifra de Cesar"
    )
    p.add_argument("--rot13", nargs=1, metavar="TEXTO", help="ROT13")
    p.add_argument("--binario", nargs=1, metavar="TEXTO", help="Codifica em binario")
    p.add_argument("--morse", nargs=1, metavar="TEXTO", help="Codifica em Morse")
    p.add_argument(
        "--vigenere", nargs=2, metavar=("CHAVE", "TEXTO"), help="Cifra de Vigenere"
    )
    p.add_argument("--atbash", nargs=1, metavar="TEXTO", help="Cifra Atbash")
    p.add_argument("--xor", nargs=2, metavar=("CHAVE", "TEXTO"), help="Cifra XOR")

    # decifrar
    p = subanalisadores.add_parser("decifrar", help="Decifra textos (cifras classicas)")
    p.add_argument(
        "--cesar", nargs=2, metavar=("DESLOCAMENTO", "TEXTO"),
        help="Decifra Cesar",
    )
    p.add_argument("--rot13", nargs=1, metavar="TEXTO", help="ROT13")
    p.add_argument("--binario", nargs=1, metavar="TEXTO", help="Decodifica binario")
    p.add_argument("--morse", nargs=1, metavar="TEXTO", help="Decodifica Morse")
    p.add_argument(
        "--vigenere", nargs=2, metavar=("CHAVE", "TEXTO"), help="Decifra Vigenere"
    )
    p.add_argument("--atbash", nargs=1, metavar="TEXTO", help="Decifra Atbash")
    p.add_argument("--xor", nargs=2, metavar=("CHAVE", "TEXTO"), help="Decifra XOR")

    # criptar
    p = subanalisadores.add_parser("criptar", help="Aplica hash ou codificacao")
    for algoritmo in [
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3",
        "blake2",
    ]:
        p.add_argument(
            f"--{algoritmo}", nargs=1, metavar="TEXTO", help=f"Hash {algoritmo.upper()}"
        )
    p.add_argument("--bcrypt", nargs=1, metavar="TEXTO", help="Hash bcrypt")
    p.add_argument("--base64", nargs=1, metavar="TEXTO", help="Codifica Base64")
    p.add_argument("--url", nargs=1, metavar="TEXTO", help="Codifica URL")
    p.add_argument("--hex", nargs=1, metavar="TEXTO", help="Codifica hexadecimal")

    # decriptar
    p = subanalisadores.add_parser("decriptar", help="Decodifica textos")
    p.add_argument("--base64", nargs=1, metavar="TEXTO", help="Decodifica Base64")
    p.add_argument("--url", nargs=1, metavar="TEXTO", help="Decodifica URL")
    p.add_argument("--hex", nargs=1, metavar="TEXTO", help="Decodifica hexadecimal")

    # manipular
    p = subanalisadores.add_parser("manipular", help="Manipula strings")
    for operacao in [
        "maiusculo",
        "minusculo",
        "titulo",
        "capitalizar",
        "camel-case",
        "pascal-case",
        "snake-case",
        "kebab-case",
        "remover-acentos",
        "remover-espacos",
        "remover-especiais",
        "apenas-digitos",
        "apenas-letras",
        "slugificar",
        "inverter",
        "contar-caracteres",
        "contar-palavras",
    ]:
        ajuda = operacao.replace("-", " ")
        if operacao in ("camel-case", "pascal-case", "snake-case", "kebab-case"):
            ajuda = operacao
        p.add_argument(f"--{operacao}", nargs=1, metavar="TEXTO", help=ajuda)
    p.add_argument(
        "--truncar", nargs=2, metavar=("COMPRIMENTO", "TEXTO"), help="Trunca texto"
    )
    p.add_argument(
        "--centralizar", nargs=3, metavar=("LARGURA", "CARACTERE", "TEXTO"),
        help="Centraliza texto",
    )

    argumentos = parser.parse_args()

    if argumentos.versao:
        from braz import __version__
        print(f"braz v{__version__}")
        return

    if not argumentos.modulo:
        parser.print_help()
        sys.exit(1)

    try:
        _rotear(argumentos)
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)


def _rotear(argumentos: argparse.Namespace) -> None:
    manipulador = {
        "gerar": _handle_gerar,
        "validar": _handle_validar,
        "cifrar": _handle_cifrar,
        "decifrar": _handle_decifrar,
        "criptar": _handle_criptar,
        "decriptar": _handle_decriptar,
        "manipular": _handle_manipular,
    }
    funcao = manipulador.get(argumentos.modulo)
    if funcao:
        funcao(argumentos)


def _handle_gerar(argumentos: argparse.Namespace) -> None:
    from braz.gerar import (
        cep,
        cnh,
        cnpj,
        cpf,
        pis,
        placa,
        renavam,
        rg,
        senha,
        telefone,
        titulo,
        uuid,
    )

    formatar = argumentos.formatar

    mapeamento = {
        "cpf": ("CPF", cpf.cpf),
        "cnpj": ("CNPJ", cnpj.cnpj),
        "rg": ("RG", rg.rg),
        "cnh": ("CNH", cnh.cnh),
        "pis": ("PIS", pis.pis),
        "titulo": ("Titulo", titulo.titulo),
        "renavam": ("RENAVAM", renavam.renavam),
        "cep": ("CEP", cep.cep),
        "telefone": ("Telefone", telefone.telefone),
        "placa": ("Placa", placa.placa),
        "uuid": ("UUID", uuid.uuid4),
    }

    for chave, (rotulo, funcao) in mapeamento.items():
        if getattr(argumentos, chave, False):
            print(f"{rotulo}: {funcao(formatar=formatar)}")
            return

    if argumentos.senha is not None:
        comprimento = argumentos.senha if isinstance(argumentos.senha, int) else 16
        print(f"Senha: {senha.senha(comprimento, formatar=formatar)}")
        return

    print("Use: braz gerar --cpf (ou --cnpj, --rg, ...)", file=sys.stderr)
    sys.exit(1)


def _handle_validar(argumentos: argparse.Namespace) -> None:
    from braz.validar import cep, cnh, cnpj, cpf, email, pis, rg, telefone

    for documento, funcao in [
        ("cpf", cpf.cpf),
        ("cnpj", cnpj.cnpj),
        ("rg", rg.rg),
        ("cnh", cnh.cnh),
        ("pis", pis.pis),
        ("cep", cep.cep),
        ("email", email.email),
        ("telefone", telefone.telefone),
    ]:
        valor = getattr(argumentos, documento, None)
        if valor:
            resultado = funcao(valor[0])
            print("Valido" if resultado else "Invalido")
            return

    print("Use: braz validar --cpf 52998224725", file=sys.stderr)
    sys.exit(1)


def _handle_cifrar(argumentos: argparse.Namespace) -> None:
    from braz.cifras import atbash, binario, cesar, morse, rot13, vigenere, xor

    if argumentos.cesar:
        deslocamento, texto = int(argumentos.cesar[0]), argumentos.cesar[1]
        print(cesar.cifrar(texto, deslocamento))
    elif argumentos.rot13:
        print(rot13.cifrar(argumentos.rot13[0]))
    elif argumentos.binario:
        print(binario.cifrar(argumentos.binario[0]))
    elif argumentos.morse:
        print(morse.cifrar(argumentos.morse[0]))
    elif argumentos.vigenere:
        chave, texto = argumentos.vigenere[0], argumentos.vigenere[1]
        print(vigenere.cifrar(texto, chave))
    elif argumentos.atbash:
        print(atbash.cifrar(argumentos.atbash[0]))
    elif argumentos.xor:
        chave, texto = argumentos.xor[0], argumentos.xor[1]
        print(xor.cifrar(texto, chave))
    else:
        print("Use: braz cifrar --cesar 5 TEXTO", file=sys.stderr)
        sys.exit(1)


def _handle_decifrar(argumentos: argparse.Namespace) -> None:
    from braz.cifras import atbash, binario, cesar, morse, rot13, vigenere, xor

    if argumentos.cesar:
        deslocamento, texto = int(argumentos.cesar[0]), argumentos.cesar[1]
        print(cesar.decifrar(texto, deslocamento))
    elif argumentos.rot13:
        print(rot13.decifrar(argumentos.rot13[0]))
    elif argumentos.binario:
        print(binario.decifrar(argumentos.binario[0]))
    elif argumentos.morse:
        print(morse.decifrar(argumentos.morse[0]))
    elif argumentos.vigenere:
        chave, texto = argumentos.vigenere[0], argumentos.vigenere[1]
        print(vigenere.decifrar(texto, chave))
    elif argumentos.atbash:
        print(atbash.decifrar(argumentos.atbash[0]))
    elif argumentos.xor:
        chave, texto = argumentos.xor[0], argumentos.xor[1]
        print(xor.decifrar(texto, chave))
    else:
        print("Use: braz decifrar --morse ... --- ...", file=sys.stderr)
        sys.exit(1)


def _handle_criptar(argumentos: argparse.Namespace) -> None:
    from braz.criptografia import (
        base64,
        bcrypt,
        blake2,
        hex,
        md5,
        sha1,
        sha3,
        sha224,
        sha256,
        sha384,
        sha512,
        url,
    )

    mapeamento = {
        "md5": md5.md5,
        "sha1": sha1.sha1,
        "sha224": sha224.sha224,
        "sha256": sha256.sha256,
        "sha384": sha384.sha384,
        "sha512": sha512.sha512,
        "blake2": blake2.blake2b,
        "bcrypt": bcrypt.bcrypt,
        "base64": base64.codificar,
        "url": url.codificar,
        "hex": hex.codificar,
    }

    for chave, funcao in mapeamento.items():
        valor = getattr(argumentos, chave, None)
        if valor:
            print(funcao(valor[0]))
            return

    if argumentos.sha3:
        print(sha3.sha3_256(argumentos.sha3[0]))
        return

    print("Use: braz criptar --sha256 TEXTO", file=sys.stderr)
    sys.exit(1)


def _handle_decriptar(argumentos: argparse.Namespace) -> None:
    from braz.criptografia import base64, hex, url

    if argumentos.base64:
        print(base64.decodificar(argumentos.base64[0]))
    elif argumentos.url:
        print(url.decodificar(argumentos.url[0]))
    elif argumentos.hex:
        print(hex.decodificar(argumentos.hex[0]))
    else:
        print("Use: braz decriptar --base64 SGVsbG8=", file=sys.stderr)
        sys.exit(1)


def _handle_manipular(argumentos: argparse.Namespace) -> None:
    from braz.strings import case, clean, utils

    mapeamento = {
        "maiusculo": (case.upper, 1),
        "minusculo": (case.lower, 1),
        "titulo": (case.title, 1),
        "capitalizar": (case.capitalize, 1),
        "camel_case": (case.camel_case, 1),
        "pascal_case": (case.pascal_case, 1),
        "snake_case": (case.snake_case, 1),
        "kebab_case": (case.kebab_case, 1),
        "remover_acentos": (clean.remove_accents, 1),
        "remover_espacos": (clean.remove_spaces, 1),
        "remover_especiais": (clean.remove_special_chars, 1),
        "apenas_digitos": (clean.apenas_digitos, 1),
        "apenas_letras": (clean.apenas_letras, 1),
        "slugificar": (utils.slug, 1),
        "inverter": (utils.reverse, 1),
        "contar_caracteres": (utils.count_chars, 1),
        "contar_palavras": (utils.count_words, 1),
    }

    for chave, (funcao, _) in mapeamento.items():
        valor = getattr(argumentos, chave, None)
        if valor:
            print(funcao(valor[0]))
            return

    if argumentos.truncar:
        comprimento, texto = int(argumentos.truncar[0]), argumentos.truncar[1]
        print(utils.truncate(texto, comprimento))
        return

    if argumentos.centralizar:
        largura = int(argumentos.centralizar[0])
        caractere = argumentos.centralizar[1]
        texto = argumentos.centralizar[2]
        print(utils.pad(texto, largura, caractere))
        return

    print("Use: braz manipular --slugificar 'Meu Texto'", file=sys.stderr)
    sys.exit(1)
