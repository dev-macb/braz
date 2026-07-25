"""Testes para funcoes de hash (MD5, SHA1, SHA2, SHA3, BLAKE2).

Usa valores conhecidos para verificar consistencia.
"""

from braz.criptografia import blake2, md5, sha1, sha3, sha224, sha256, sha384, sha512

TEXTO = "hello"
# Valores pre-calculados
MD5_HELLO = "5d41402abc4b2a76b9719d911017c592"
SHA1_HELLO = "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"
SHA224_HELLO = "ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193"
SHA256_HELLO = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
SHA384_HELLO = (
    "59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa"
    "90125a3c79f90397bdf5f6a13de828684f"
)
SHA512_HELLO = (
    "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca7"
    "2323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"
)


def test_md5():
    assert md5.md5(TEXTO) == MD5_HELLO


def test_sha1():
    assert sha1.sha1(TEXTO) == SHA1_HELLO


def test_sha224():
    assert sha224.sha224(TEXTO) == SHA224_HELLO


def test_sha256():
    assert sha256.sha256(TEXTO) == SHA256_HELLO


def test_sha384():
    assert sha384.sha384(TEXTO) == SHA384_HELLO


def test_sha512():
    assert sha512.sha512(TEXTO) == SHA512_HELLO


def test_sha3_256():
    result = sha3.sha3_256(TEXTO)
    assert len(result) == 64  # 256 bits em hex = 64 chars
    assert isinstance(result, str)


def test_sha3_512():
    result = sha3.sha3_512(TEXTO)
    assert len(result) == 128  # 512 bits em hex = 128 chars


def test_blake2b():
    result = blake2.blake2b(TEXTO)
    assert len(result) == 128  # 64 bytes em hex = 128 chars


def test_blake2s():
    result = blake2.blake2s(TEXTO)
    assert len(result) == 64  # 32 bytes em hex = 64 chars


def test_hashes_diferentes():
    assert md5.md5(TEXTO) != sha256.sha256(TEXTO)


def test_hash_vazio():
    assert len(md5.md5("")) == 32
    assert len(sha256.sha256("")) == 64
