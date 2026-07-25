"""Testes para CEP, Telefone, Email e Placa."""

import re

from braz.gerar import cep, placa, telefone
from braz.validar import cep as validar_cep
from braz.validar import email as validar_email
from braz.validar import telefone as validar_telefone


def test_gerar_cep_formato():
    numero = cep.cep()
    assert re.fullmatch(r"\d{5}-\d{3}", numero)


def test_gerar_cep_valido():
    for _ in range(10):
        assert validar_cep.cep(cep.cep())


def test_validar_cep_sem_mascara():
    assert validar_cep.cep("12345678")


def test_validar_cep_com_mascara():
    assert validar_cep.cep("12345-678")


def test_validar_cep_invalido():
    assert not validar_cep.cep("1234-567")


def test_validar_cep_vazio():
    assert not validar_cep.cep("")


def test_gerar_telefone():
    numero = telefone.telefone()
    assert "(" in numero and ")" in numero


def test_validar_telefone_valido():
    assert validar_telefone.telefone("(11) 91234-5678")


def test_validar_telefone_10_digitos():
    assert validar_telefone.telefone("113456-7890")


def test_validar_telefone_invalido():
    assert not validar_telefone.telefone("123")


def test_validar_telefone_vazio():
    assert not validar_telefone.telefone("")


def test_gerar_placa():
    placa_str = placa.placa()
    assert re.fullmatch(r"[A-Z]{3}-\d{4}", placa_str)


def test_validar_email_valido():
    assert validar_email.email("usuario@exemplo.com")


def test_validar_email_sem_arroba():
    assert not validar_email.email("usuarioexemplo.com")


def test_validar_email_sem_dominio():
    assert not validar_email.email("usuario@")


def test_validar_email_vazio():
    assert not validar_email.email("")
