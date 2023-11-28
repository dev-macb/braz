# Importe as classes Braz e Validar
from gerar import Gerar
from validar import Validar


cpf = Gerar.cpf(False)
print(f'cpf: {cpf}\n')

if Validar.cpf(cpf):
    print(f'[*] O cpf é válido.\n')
else:
    print(f'[*] O cpf é inválido!\n')