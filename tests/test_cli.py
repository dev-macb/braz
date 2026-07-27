"""Testes para a interface de linha de comando (CLI)."""

import io
import re
import sys

from braz import __version__


def _executar_cli(*argumentos: str) -> str:
    """Executa a CLI com os argumentos fornecidos e retorna a saida."""
    from braz.cli.app import main

    stdout_capturado = io.StringIO()
    stderr_capturado = io.StringIO()
    stdout_original = sys.stdout
    stderr_original = sys.stderr
    argv_original = sys.argv

    sys.argv = ["braz", *argumentos]
    sys.stdout = stdout_capturado
    sys.stderr = stderr_capturado

    try:
        main()
    except SystemExit:
        pass
    finally:
        sys.stdout = stdout_original
        sys.stderr = stderr_original
        sys.argv = argv_original

    saida = stdout_capturado.getvalue()
    if saida:
        return saida.rstrip("\n")
    return stderr_capturado.getvalue().rstrip("\n")


def test_cli_versao_curta():
    saida = _executar_cli("-v")
    assert saida == f"braz v{__version__}"


def test_cli_versao_longa():
    saida = _executar_cli("--versao")
    assert saida == f"braz v{__version__}"


def test_cli_gerar_cpf_sem_formato():
    saida = _executar_cli("gerar", "--cpf")
    assert saida.startswith("CPF: ")
    valor = saida.removeprefix("CPF: ")
    assert re.fullmatch(r"\d{11}", valor)


def test_cli_gerar_cpf_com_formato():
    saida = _executar_cli("gerar", "--cpf", "-f")
    assert saida.startswith("CPF: ")
    valor = saida.removeprefix("CPF: ")
    assert re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", valor)


def test_cli_gerar_cnpj_sem_formato():
    saida = _executar_cli("gerar", "--cnpj")
    assert saida.startswith("CNPJ: ")
    valor = saida.removeprefix("CNPJ: ")
    assert re.fullmatch(r"\d{14}", valor)


def test_cli_gerar_cnpj_com_formato():
    saida = _executar_cli("gerar", "--cnpj", "--formatar")
    assert saida.startswith("CNPJ: ")
    valor = saida.removeprefix("CNPJ: ")
    assert re.fullmatch(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", valor)


def test_cli_gerar_cep_sem_formato():
    saida = _executar_cli("gerar", "--cep")
    assert saida.startswith("CEP: ")
    valor = saida.removeprefix("CEP: ")
    assert re.fullmatch(r"\d{8}", valor)


def test_cli_gerar_cep_com_formato():
    saida = _executar_cli("gerar", "--cep", "-f")
    assert saida.startswith("CEP: ")
    valor = saida.removeprefix("CEP: ")
    assert re.fullmatch(r"\d{5}-\d{3}", valor)


def test_cli_gerar_senha_sem_formato():
    saida = _executar_cli("gerar", "--senha", "8")
    assert saida.startswith("Senha: ")
    valor = saida.removeprefix("Senha: ")
    assert len(valor) == 8


def test_cli_gerar_senha_com_formato():
    saida = _executar_cli("gerar", "--senha", "12", "-f")
    assert saida.startswith("Senha: ")
    valor = saida.removeprefix("Senha: ")
    assert len(valor) == 12


def test_cli_sem_modulo_exibe_ajuda():
    saida = _executar_cli()
    assert "usage:" in saida.lower() or "Usage:" in saida
