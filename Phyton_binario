import math

# 1) Quantização
def quantizacao(niveis):
    bits = math.ceil(math.log2(niveis))
    combinacoes = []

    for i in range(2**bits):
        combinacoes.append(format(i, f'0{bits}b'))

    return bits, combinacoes


# 2) Decimal → Binário
def decimal_para_binario(num):
    return bin(num)[2:]


# 3) Decimal fracionário → Binário
def decimal_fracionario_para_binario(num, precisao=10):
    inteiro = int(num)
    fracao = num - inteiro

    bin_inteiro = bin(inteiro)[2:]
    bin_fracao = ""

    while fracao > 0 and len(bin_fracao) < precisao:
        fracao *= 2
        bit = int(fracao)
        bin_fracao += str(bit)
        fracao -= bit

    return f"{bin_inteiro}.{bin_fracao}"


# Binário → Decimal
def binario_para_decimal(binario):
    if '.' in binario:
        inteiro, fracao = binario.split('.')
    else:
        inteiro, fracao = binario, ''

    decimal = int(inteiro, 2)

    for i, bit in enumerate(fracao):
        decimal += int(bit) * (2 ** -(i+1))

    return decimal


# Octal ↔ Binário
def octal_para_binario(octal):
    return bin(int(octal, 8))[2:]

def binario_para_octal(binario):
    return oct(int(binario, 2))[2:]


# Hexa ↔ Binário
def hexa_para_binario(hexa):
    return bin(int(hexa, 16))[2:]

def binario_para_hexa(binario):
    return hex(int(binario, 2))[2:]


# Conversão geral → Decimal via binário
def qualquer_para_decimal(valor, base):
    binario = bin(int(valor, base))[2:]
    decimal = int(binario, 2)
    return binario, decimal