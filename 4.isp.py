"""
Interface Segregation Principle
Crie interfaces que são específicas. Clientes não devem depender de interfaces que eles não usarão
"""
from abc import ABC

class IJanela(ABC): 
    def fechar(self):
        raise NotImplementedError

class IJanelaTamanhoVariavel(IJanela, ABC):
    def minimizar(self):
        pass

    def maximizar(self):
        pass

class IJanelaComMenu(IJanela, ABC):
    def mostrar_menu(self):
        pass

class JanelaTamanhoFixo(IJanelaComMenu):    
    def mostrar_menu(self):
        pass
    
    def fechar(self):
        pass

class JanelaSemMenu(IJanelaTamanhoVariavel):
    def maximizar(self):
        pass

    def minimizar(self):
        pass
    
    def fechar(self):
        pass
