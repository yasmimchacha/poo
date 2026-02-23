class contabancaria :
    def __init__(self):
        self.__saldo = 0 

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor 
        else:
            print("erro: saldo não pode ser negativo!")
            


    



