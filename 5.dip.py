"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""


from abc import ABC, abstractmethod

class AbstractStatsReporter(ABC):
    def set_player(self, player):
        self.char = player
    
    @abstractmethod
    def report(self):
        pass

class Player:
    def __init__(self, name, statsReporter: AbstractStatsReporter):
        self.__name = name
        self.__hp = 100
        self.__speed = 1
        self.reporter = statsReporter
        self.reporter.set_player(self)

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name
    
    def report(self):
        self.reporter.report()

class StatsReporter(AbstractStatsReporter):
    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')

class StatsReporterWithColor(AbstractStatsReporter):
    def report(self):
        print(f'\033[31mName:{self.char.name()}\033[0;0m')
        print(f'\033[32mHP:{self.char.hp()}\033[31m')
