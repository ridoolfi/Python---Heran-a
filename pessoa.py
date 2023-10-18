class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__logradouro = ""
        self.__bairro = ""
        self.__cidade = ""
        self.__estado = ""
        self.__cep = ""
        self.__email = ""
        self.__telefone = ""

    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nm):
        self.__nome = nm

    @property
    def logradouro(self):
        return self.__logradouro

    @logradouro.setter
    def logradouro(self, lg):
        self.__logradouro = lg
    
    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bd):
        self.__bairro = bd
    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cd):
        self.__cidade = cd

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, es):
        self.__estado = es
    
    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, tel):
        self.__telefone = tel
    
    
