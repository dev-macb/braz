# -*- coding: utf-8 -*-


""" Esse módulo contém todas as funções de criptografia do pacote braz. """


# Importação de módulos
import base64


def b32(mensagem: str) -> str:
    if not mensagem:
        return None
    msg_string = mensagem.encode('ascii')
    msg_cripto = base64.b32encode(msg_string)
    
    return msg_cripto.decode('utf-8')
