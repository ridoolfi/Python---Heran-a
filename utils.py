from pessoa__fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

def dadosP(p):
    p.nome = input("Nome: ")
    p.logradouro = input("Logradouro: ")
    p.bairro = input("Bairro: ")
    p.cidade = input("Cidade: ")
    p.estado = input("Estado: ")
    p.cep = input("Cep: ")
    p.email = input("Email: ")
    p.telefone = input("Telefone: ")



def dadosPF(pf):
    dadosP(pf)
    pf.rg = input("RG: ")
    pf.cpf = input("CPF: ")

def dadosPJ(pj):
    dadosP(pj)
    pj.cnpj = input("CNPJ: ")
    pj.ie = input("IE: ")
    pj.im = input("IM: ")

def printP(p):
    print("=-=-=-=-=-=-=-=-=")
    print("NOME: ", p.nome)
    print("LOGRADOURO: ", p.logradouro)
    print("BAIRRO: ", p.bairro)
    print("CIDADE: ", p.cidade)
    print("ESTADO: ", p.estado)
    print("CEP: ", p.cep)
    print("EMAIL: ", p.email)
    print("TELEFONE: ", p.telefone)

def printPF(pf):
    printP(pf)
    print(pf.cpf)
    print(pf.rg)

def printPJ(pj):
    print(pj)
    print(pj.cnpj)
    print(pj.ie)
    print(pj.im)

def localizarPF(dados, cpf):
    for i in range(len(dados)):
        if isinstance(dados[i], PessoaFisica) and dados[i].cpf == cpf:
            return i
    return -1
    
def localizaPJ(dados, pj):
    for i in range(len(dados)):
        if isinstance(dados[i], PessoaJuridica) and dados[i].cnpj == pj:
            return i
    return -1
