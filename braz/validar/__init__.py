# -*- coding: utf-8 -*-


""" Esse módulo contém o construtor do módulo gerar do pacote. """


# Importações do braz
from braz.gerar.rg import ver_rg
from braz.gerar.ie import ver_ie
from braz.gerar.cpf import ver_cpf
from braz.gerar.cnpj import ver_cnpj
from braz.gerar.senha import ver_senha
from braz.gerar.renavam import ver_renavam
from braz.gerar.pis_pasep import ver_pis_pasep
from braz.gerar.titulo_eleitor import ver_titulo_eleitor


# Importação genérica do pacote braz
__all__ = [
    'ver_rg',
    'ver_ie',
    'ver_cpf',
    'ver_cnpj',
    'ver_senha',
    'ver_renavam',
    'ver_pis_pasep',
    'ver_titulo_eleitor'
]
