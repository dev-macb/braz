# -*- coding: utf-8 -*-


""" Esse módulo contém todas as funções de criptografia do pacote braz. """


# Importação de módulos
import base64


def de_b16(mensagem: str) -> str:
    if not mensagem:
        return None
    msg_string = mensagem.encode('utf-8').upper()
    msg_cripto = base64.b16decode(msg_string)
    
    return msg_cripto.decode('utf-8')

print(de_b16('4D204120432042'))