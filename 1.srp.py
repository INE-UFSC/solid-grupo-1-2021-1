"""
Single Responsibility Principle

Uma classe deve ter somente uma responsabilidade
ou
Uma classe deve ter somente um motivo para mudar
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

class AnimalDB:
    def __init__(self, animal: Animal):
        self.animal = animal
    
    def save(self):
        print(f"Saving animal {self.animal.get_name()}")