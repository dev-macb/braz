"""Testes para RG, CNH, PIS, Titulo e RENAVAM (geracao + validacao)."""

from braz.gerar import cnh, pis, renavam, rg, titulo
from braz.validar import cnh as validar_cnh
from braz.validar import pis as validar_pis
from braz.validar import rg as validar_rg


def test_gerar_rg():
    numero = rg.rg()
    assert len(numero) == 9


def test_gerar_rg_valido():
    for _ in range(10):
        assert validar_rg.rg(rg.rg())


def test_validar_rg_tamanho_incorreto():
    assert not validar_rg.rg("12345678")


def test_validar_rg_vazio():
    assert not validar_rg.rg("")


def test_gerar_cnh():
    numero = cnh.cnh()
    assert len(numero) == 11
    assert numero.isdigit()


def test_gerar_cnh_valido():
    for _ in range(10):
        assert validar_cnh.cnh(cnh.cnh())


def test_validar_cnh_tamanho_incorreto():
    assert not validar_cnh.cnh("123")


def test_validar_cnh_vazio():
    assert not validar_cnh.cnh("")


def test_gerar_pis():
    numero = pis.pis()
    assert len(numero) == 11
    assert numero.isdigit()


def test_gerar_pis_valido():
    for _ in range(10):
        assert validar_pis.pis(pis.pis())


def test_validar_pis_digitos_iguais():
    assert not validar_pis.pis("11111111111")


def test_gerar_titulo():
    numero = titulo.titulo()
    assert len(numero) == 14
    assert numero.isdigit()


def test_gerar_renavam():
    numero = renavam.renavam()
    assert len(numero) == 10
    assert numero.isdigit()
