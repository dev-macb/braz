from braz.shared.digit import calcular_digito_verificador
from braz.shared.helpers import todos_mesmo_digito, apenas_digitos


def test_apenas_digitos():
    assert apenas_digitos("abc123def456") == "123456"


def test_apenas_digitos_vazio():
    assert apenas_digitos("") == ""


def test_apenas_digitos_sem_numeros():
    assert apenas_digitos("abc") == ""


def test_todos_mesmo_digito_verdadeiro():
    assert todos_mesmo_digito("11111")


def test_todos_mesmo_digito_falso():
    assert not todos_mesmo_digito("12345")


def test_todos_mesmo_digito_vazio():
    assert not todos_mesmo_digito("")


def test_calcular_digito_verificador():
    base = [0, 1, 1, 2, 3, 4, 5, 6, 7]
    pesos = list(range(10, 1, -1))
    resultado = calcular_digito_verificador(base, pesos)
    assert isinstance(resultado, int)
    assert 0 <= resultado <= 9


def test_calcular_digito_verificador_resto_0():
    base = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    pesos = list(range(10, 1, -1))
    assert calcular_digito_verificador(base, pesos) == 0
