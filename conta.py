class Conta:

    #Construtor:
    def __init__(self, numero, titular, saldo, limite = 100.0):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Metodos:
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor

        else:
            print('O valor {} passou o limite'.format(format(valor)))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}



""" 

    `__init__` inicia a função num local da memória
    variável `self` armazena qual o local da memória a função está alocada

    para acessar um atributo no console, apenas inicie a classe e depois 
    utilize `.` para acessar o método que for; 
    ex:
    ```

    conta = Conta(numero = "00001", titular = "João", saldo = 1000.0)
    print(conta.saldo)

    >> 1000.0

    ```


    Para coesão, sempre usar o self. na classe, nao usar outro nome para nao 
    bagunçar a sintaxe e a legibilidade do código

"""