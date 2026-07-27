def calcular_digito_verificador(base: list[int], pesos: list[int]) -> int:
    """Calcula um digito verificador usando soma ponderada modulo 11."""
    total = sum(d * p for d, p in zip(base, pesos))
    resto = total % 11
    return 0 if resto < 2 else 11 - resto


CPF_WEIGHTS_1 = list(range(10, 1, -1))
CPF_WEIGHTS_2 = list(range(11, 1, -1))

CNPJ_WEIGHTS_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
CNPJ_WEIGHTS_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

CNH_WEIGHTS_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
CNH_WEIGHTS_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

PIS_WEIGHTS = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

TITULO_WEIGHTS_1 = [2, 3, 4, 5, 6, 7, 8, 9]
TITULO_WEIGHTS_2 = [3, 4, 5, 6, 7, 8, 9, 10, 11]

RENAVAM_WEIGHTS = [2, 3, 4, 5, 6, 7, 8, 9]
