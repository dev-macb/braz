"""Testes para UUID e Senha."""

import uuid as _uuid

from braz.gerar import senha, uuid


def test_gerar_uuid_formato():
    uid = uuid.uuid4()
    # Tenta parsear como UUID v4
    parsed = _uuid.UUID(uid)
    assert str(parsed) == uid


def test_gerar_uuid_unico():
    assert uuid.uuid4() != uuid.uuid4()


def test_gerar_senha_tamanho_padrao():
    assert len(senha.senha()) == 16


def test_gerar_senha_tamanho_personalizado():
    assert len(senha.senha(32)) == 32
    assert len(senha.senha(8)) == 8


def test_gerar_senha_tamanho_0():
    assert senha.senha(0) == ""


def test_gerar_senha_caracteres_validos():
    pwd = senha.senha()
    assert all(c in senha.ASCII for c in pwd)
