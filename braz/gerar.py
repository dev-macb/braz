import random

class Gerar:
    @staticmethod
    def cpf(formatar = False) -> str:
        cpf = [random.randrange(10) for _ in range(9)]

        for _ in range(2):
            value = sum((len(cpf) + 1 - i) * v for i, v in enumerate(cpf)) % 11
            cpf.append(11 - value if value > 1 else 0)

        if formatar:
            return f'{cpf[1:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        
        return "".join(map(str, cpf))
    

    @staticmethod
    def cnpj(formatar = False) -> str:
        cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

        for _ in range(2):
            value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
            digit = 11 - value % 11
            cnpj.append(digit if digit < 10 else 0)

        if formatar:
            return f"{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
        else:
            return "".join(map(str, cnpj))


    @staticmethod
    def rg(formatar = False) -> str:
        rg = [random.randrange(10) for _ in range(9)]

        if formatar:
            return f"{rg[0:2]}.{rg[2:5]}.{rg[5:8]}"
        else:
            return "".join(map(str, rg))


    @staticmethod
    def cnh(formatar = False) -> str:
        cnh = [random.randrange(10) for _ in range(11)]

        if formatar:
            return f"{cnh[0:3]}.{cnh[3:6]}.{cnh[6:9]}-{cnh[9:]}"
        else:
            return "".join(map(str, cnh))
    