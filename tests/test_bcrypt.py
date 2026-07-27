from braz.criptografia import bcrypt


def test_bcrypt_gera_hash():
    result = bcrypt.bcrypt("senha123")
    assert result.startswith("$2")


def test_bcrypt_check_valido():
    hashed = bcrypt.bcrypt("senha123")
    assert bcrypt.verificar_bcrypt("senha123", hashed)


def test_bcrypt_check_invalido():
    hashed = bcrypt.bcrypt("senha123")
    assert not bcrypt.verificar_bcrypt("outra", hashed)
