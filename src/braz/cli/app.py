import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="braz",
        description="CLI para geracao, validacao e transformacao de dados",
    )
    subparsers = parser.add_subparsers(dest="module")

    # gerar
    p = subparsers.add_parser("gerar", help="Gera dados validos")
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
    p = subparsers.add_parser("validar", help="Valida informacoes")
    for doc in ["cpf", "cnpj", "rg", "cnh", "pis", "cep", "email", "telefone"]:
        p.add_argument(
            f"--{doc}", nargs=1, metavar="VALOR", help=f"Valida {doc.upper()}"
        )

    # cifrar
    p = subparsers.add_parser("cifrar", help="Cifra textos (cifras classicas)")
    p.add_argument(
        "--cesar", nargs=2, metavar=("SHIFT", "TEXTO"), help="Cifra de Cesar"
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
    p = subparsers.add_parser("decifrar", help="Decifra textos (cifras classicas)")
    p.add_argument("--cesar", nargs=2, metavar=("SHIFT", "TEXTO"), help="Decifra Cesar")
    p.add_argument("--rot13", nargs=1, metavar="TEXTO", help="ROT13")
    p.add_argument("--binario", nargs=1, metavar="TEXTO", help="Decodifica binario")
    p.add_argument("--morse", nargs=1, metavar="TEXTO", help="Decodifica Morse")
    p.add_argument(
        "--vigenere", nargs=2, metavar=("CHAVE", "TEXTO"), help="Decifra Vigenere"
    )
    p.add_argument("--atbash", nargs=1, metavar="TEXTO", help="Decifra Atbash")
    p.add_argument("--xor", nargs=2, metavar=("CHAVE", "TEXTO"), help="Decifra XOR")

    # criptar
    p = subparsers.add_parser("criptar", help="Aplica hash ou codificacao")
    for algo in [
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
            f"--{algo}", nargs=1, metavar="TEXTO", help=f"Hash {algo.upper()}"
        )
    p.add_argument("--bcrypt", nargs=1, metavar="TEXTO", help="Hash bcrypt")
    p.add_argument("--base64", nargs=1, metavar="TEXTO", help="Codifica Base64")
    p.add_argument("--url", nargs=1, metavar="TEXTO", help="Codifica URL")
    p.add_argument("--hex", nargs=1, metavar="TEXTO", help="Codifica hexadecimal")

    # decriptar
    p = subparsers.add_parser("decriptar", help="Decodifica textos")
    p.add_argument("--base64", nargs=1, metavar="TEXTO", help="Decodifica Base64")
    p.add_argument("--url", nargs=1, metavar="TEXTO", help="Decodifica URL")
    p.add_argument("--hex", nargs=1, metavar="TEXTO", help="Decodifica hexadecimal")

    # manipular
    p = subparsers.add_parser("manipular", help="Manipula strings")
    for op in [
        "upper",
        "lower",
        "title",
        "capitalize",
        "camel-case",
        "pascal-case",
        "snake-case",
        "kebab-case",
        "remove-accents",
        "remove-spaces",
        "remove-special-chars",
        "only-digits",
        "only-letters",
        "slug",
        "reverse",
        "count-chars",
        "count-words",
    ]:
        p.add_argument(f"--{op}", nargs=1, metavar="TEXTO", help=op.replace("-", " "))
    p.add_argument(
        "--truncate", nargs=2, metavar=("LENGTH", "TEXTO"), help="Trunca texto"
    )
    p.add_argument(
        "--pad", nargs=3, metavar=("WIDTH", "CHAR", "TEXTO"), help="Centraliza texto"
    )

    args = parser.parse_args()

    if not args.module:
        parser.print_help()
        sys.exit(1)

    try:
        _route(args)
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)


def _route(args: argparse.Namespace) -> None:
    handler = {
        "gerar": _handle_gerar,
        "validar": _handle_validar,
        "cifrar": _handle_cifrar,
        "decifrar": _handle_decifrar,
        "criptar": _handle_criptar,
        "decriptar": _handle_decriptar,
        "manipular": _handle_manipular,
    }
    fn = handler.get(args.module)
    if fn:
        fn(args)


def _handle_gerar(args: argparse.Namespace) -> None:
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
    from braz.shared import formatters

    labels = {
        "cpf": "CPF",
        "cnpj": "CNPJ",
        "rg": "RG",
        "cnh": "CNH",
        "pis": "PIS",
        "titulo": "Titulo",
        "renavam": "RENAVAM",
        "cep": "CEP",
        "telefone": "Telefone",
        "placa": "Placa",
        "uuid": "UUID",
    }

    mapping = {
        "cpf": cpf.cpf,
        "cnpj": cnpj.cnpj,
        "rg": rg.rg,
        "cnh": cnh.cnh,
        "pis": pis.pis,
        "titulo": titulo.titulo,
        "renavam": renavam.renavam,
        "cep": cep.cep,
        "telefone": telefone.telefone,
        "placa": placa.placa,
        "uuid": uuid.uuid4,
    }

    for key, fn in mapping.items():
        if getattr(args, key, False):
            valor = fn()
            fmt = getattr(formatters, key, None)
            if fmt:
                valor = fmt(valor)
            print(f"{labels[key]}: {valor}")
            return

    if args.senha is not None:
        length = args.senha if isinstance(args.senha, int) else 16
        valor = senha.senha(length)
        print(f"Senha: {valor}")
        return

    print("Use: braz gerar --cpf (ou --cnpj, --rg, ...)", file=sys.stderr)
    sys.exit(1)


def _handle_validar(args: argparse.Namespace) -> None:
    from braz.validar import cep, cnh, cnpj, cpf, email, pis, rg, telefone

    for doc, fn in [
        ("cpf", cpf.cpf),
        ("cnpj", cnpj.cnpj),
        ("rg", rg.rg),
        ("cnh", cnh.cnh),
        ("pis", pis.pis),
        ("cep", cep.cep),
        ("email", email.email),
        ("telefone", telefone.telefone),
    ]:
        val = getattr(args, doc, None)
        if val:
            result = fn(val[0])
            print("Valido" if result else "Invalido")
            return

    print("Use: braz validar --cpf 52998224725", file=sys.stderr)
    sys.exit(1)


def _handle_cifrar(args: argparse.Namespace) -> None:
    from braz.cifras import atbash, binario, cesar, morse, rot13, vigenere, xor

    if args.cesar:
        shift, texto = int(args.cesar[0]), args.cesar[1]
        print(cesar.encrypt(texto, shift))
    elif args.rot13:
        print(rot13.encrypt(args.rot13[0]))
    elif args.binario:
        print(binario.encrypt(args.binario[0]))
    elif args.morse:
        print(morse.encrypt(args.morse[0]))
    elif args.vigenere:
        chave, texto = args.vigenere[0], args.vigenere[1]
        print(vigenere.encrypt(texto, chave))
    elif args.atbash:
        print(atbash.encrypt(args.atbash[0]))
    elif args.xor:
        chave, texto = args.xor[0], args.xor[1]
        print(xor.encrypt(texto, chave))
    else:
        print("Use: braz cifrar --cesar 5 TEXTO", file=sys.stderr)
        sys.exit(1)


def _handle_decifrar(args: argparse.Namespace) -> None:
    from braz.cifras import atbash, binario, cesar, morse, rot13, vigenere, xor

    if args.cesar:
        shift, texto = int(args.cesar[0]), args.cesar[1]
        print(cesar.decrypt(texto, shift))
    elif args.rot13:
        print(rot13.decrypt(args.rot13[0]))
    elif args.binario:
        print(binario.decrypt(args.binario[0]))
    elif args.morse:
        print(morse.decrypt(args.morse[0]))
    elif args.vigenere:
        chave, texto = args.vigenere[0], args.vigenere[1]
        print(vigenere.decrypt(texto, chave))
    elif args.atbash:
        print(atbash.decrypt(args.atbash[0]))
    elif args.xor:
        chave, texto = args.xor[0], args.xor[1]
        print(xor.decrypt(texto, chave))
    else:
        print("Use: braz decifrar --morse ... --- ...", file=sys.stderr)
        sys.exit(1)


def _handle_criptar(args: argparse.Namespace) -> None:
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

    mapping = {
        "md5": md5.md5,
        "sha1": sha1.sha1,
        "sha224": sha224.sha224,
        "sha256": sha256.sha256,
        "sha384": sha384.sha384,
        "sha512": sha512.sha512,
        "blake2": blake2.blake2b,
        "bcrypt": bcrypt.bcrypt,
        "base64": base64.encode,
        "url": url.encode,
        "hex": hex.encode,
    }

    for key, fn in mapping.items():
        val = getattr(args, key, None)
        if val:
            print(fn(val[0]))
            return

    if args.sha3:
        print(sha3.sha3_256(args.sha3[0]))
        return

    print("Use: braz criptar --sha256 TEXTO", file=sys.stderr)
    sys.exit(1)


def _handle_decriptar(args: argparse.Namespace) -> None:
    from braz.criptografia import base64, hex, url

    if args.base64:
        print(base64.decode(args.base64[0]))
    elif args.url:
        print(url.decode(args.url[0]))
    elif args.hex:
        print(hex.decode(args.hex[0]))
    else:
        print("Use: braz decriptar --base64 SGVsbG8=", file=sys.stderr)
        sys.exit(1)


def _handle_manipular(args: argparse.Namespace) -> None:
    from braz.strings import case, clean, utils

    mapping = {
        "upper": (case.upper, 1),
        "lower": (case.lower, 1),
        "title": (case.title, 1),
        "capitalize": (case.capitalize, 1),
        "camel_case": (case.camel_case, 1),
        "pascal_case": (case.pascal_case, 1),
        "snake_case": (case.snake_case, 1),
        "kebab_case": (case.kebab_case, 1),
        "remove_accents": (clean.remove_accents, 1),
        "remove_spaces": (clean.remove_spaces, 1),
        "remove_special_chars": (clean.remove_special_chars, 1),
        "only_digits": (clean.only_digits, 1),
        "only_letters": (clean.only_letters, 1),
        "slug": (utils.slug, 1),
        "reverse": (utils.reverse, 1),
        "count_chars": (utils.count_chars, 1),
        "count_words": (utils.count_words, 1),
    }

    for key, (fn, _) in mapping.items():
        val = getattr(args, key, None)
        if val:
            print(fn(val[0]))
            return

    if args.truncate:
        length, texto = int(args.truncate[0]), args.truncate[1]
        print(utils.truncate(texto, length))
        return

    if args.pad:
        width, char, texto = int(args.pad[0]), args.pad[1], args.pad[2]
        print(utils.pad(texto, width, char))
        return

    print("Use: braz manipular --slug 'Meu Texto'", file=sys.stderr)
    sys.exit(1)
