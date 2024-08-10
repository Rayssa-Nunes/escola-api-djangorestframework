import re
from validate_docbr import CPF

def nome_invalido(nome):
    return not nome.isalpha()

def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def celular_invalido(celular):
    # 83 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    # print(resposta)
    return not resposta
