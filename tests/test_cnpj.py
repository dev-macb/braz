from braz.gerar import cnpj as gerar_cnpj
from braz.validar import cnpj as validar_cnpj


def test_gerar_cnpj():
    numero = gerar_cnpj.cnpj()
    assert len(numero) == 14
    assert numero.isdigit()


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
