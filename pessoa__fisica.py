from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self):
        super().__init__()
        self.__rg = ""
        self.__cpf = ""
    
    @property
    def rg(self):
        return self.__rg
    @rg.setter
    def rg(self, rg):
        self.__rg = rg
    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf