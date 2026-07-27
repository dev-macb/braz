import re

from braz.gerar import cpf as gerar_cpf
from braz.validar import cpf as validar_cpf


def test_gerar_cpf():
    numero = gerar_cpf.cpf()
    assert len(numero) == 11
    assert numero.isdigit()


def test_gerar_cpf_sem_formato():
    numero = gerar_cpf.cpf(formatar=False)
    assert re.fullmatch(r"\d{11}", numero)


def test_gerar_cpf_formatado():
    numero = gerar_cpf.cpf(formatar=True)
    assert re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", numero)


def test_gerar_cpf_valido():
    for _ in range(10):
        numero = gerar_cpf.cpf()
        assert validar_cpf.cpf(numero)


def test_validar_cpf_valido():
    assert validar_cpf.cpf("52998224725")


def test_validar_cpf_com_mascara():
    assert validar_cpf.cpf("529.982.247-25")


def test_validar_cpf_tamanho_incorreto():
    assert not validar_cpf.cpf("12345678901")


def test_validar_cpf_digitos_iguais():
    assert not validar_cpf.cpf("11111111111")


def test_validar_cpf_vazio():
    assert not validar_cpf.cpf("")


def test_validar_cpf_com_letras():
    assert not validar_cpf.cpf("abc.def.ghi-jk")
