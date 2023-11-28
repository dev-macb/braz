import re
from itertools import cycle


class Validar:
    @staticmethod
    def cpf(cpf: str) -> bool:
        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            return False

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números e se todos são diferentes
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validação dos dígitos verificadores
        for i in range(2):
            sum_of_products = sum(a * b for a, b in zip(numbers[:9 + i], range(10 + i, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10

            if numbers[9 + i] != expected_digit:
                return False

        return True



    @staticmethod
    def cnpj(cnpj: str) -> bool:
        LENGTH_CNPJ = 14

        # Verifica o comprimento do CNPJ
        if len(cnpj) != LENGTH_CNPJ:
            return False

        # Verifica se o CNPJ possui apenas dígitos repetidos
        if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
            return False

        cnpj_r = cnpj[::-1]
        for i in range(2, 0, -1):
            cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
            dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
            if cnpj_r[i - 1:i] != str(dv % 10):
                return False

        return True


    @staticmethod
    def rg(rg: str) -> bool:
        rg = re.sub(r'\D', '', rg)  # Remove caracteres não numéricos
        return rg.isdigit() and len(rg) == 9


    @staticmethod
    def  cnh(cnh: str) -> bool:
        cnh = re.sub(r'\D', '', cnh)  # Remove caracteres não numéricos
        return cnh.isdigit() and len(cnh) == 11