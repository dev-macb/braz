import re

from braz.gerar import cnpj as gerar_cnpj
from braz.validar import cnpj as validar_cnpj


def test_gerar_cnpj():
    numero = gerar_cnpj.cnpj()
    assert len(numero) == 14
    assert numero.isdigit()


def test_gerar_cnpj_sem_formato():
    numero = gerar_cnpj.cnpj(formatar=False)
    assert re.fullmatch(r"\d{14}", numero)


def test_gerar_cnpj_formatado():
    numero = gerar_cnpj.cnpj(formatar=True)
    assert re.fullmatch(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", numero)


def test_gerar_cnpj_valido():
    for _ in range(10):
        numero = gerar_cnpj.cnpj()
        assert validar_cnpj.cnpj(numero)


def test_validar_cnpj_valido():
    assert validar_cnpj.cnpj("11222333000181")


def test_validar_cnpj_com_mascara():
    assert validar_cnpj.cnpj("11.222.333/0001-81")


def test_validar_cnpj_tamanho_incorreto():
    assert not validar_cnpj.cnpj("12345678901234")


def test_validar_cnpj_digitos_iguais():
    assert not validar_cnpj.cnpj("11111111111111")


def test_validar_cnpj_vazio():
    assert not validar_cnpj.cnpj("")


def test_validar_cnpj_invalido():
    assert not validar_cnpj.cnpj("12345678901234")
