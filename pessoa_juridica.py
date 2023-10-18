from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self):
        super().__init__()
        self.__cnpj = ""
        self.__ie = ""
        self.__im = ""

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def ie(self):
        return self.__ie
    
    @ie.setter
    def ie(self, ie):
        self.__ie = ie

    @property
    def im(self):
        return self.__im
    
    @im.setter
    def im(self, im):
        self.__cnpj = im
    