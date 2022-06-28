from abc import ABC, abstractclassmethod

class ElevState(ABC):
    @abstractclassmethod
    def state(self):
        pass