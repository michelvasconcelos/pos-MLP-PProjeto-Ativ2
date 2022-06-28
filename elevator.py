from typing import Type
from elevState import ElevState
from elevUp import ElevUp
from elevDown import ElevDown
from elevStop import ElevStop
from elevStuck import ElevStuck
from elevIdle import ElevIdle

class Elevator():
    def __init__(self, state_option: Type[ElevState]) -> None:
        self.state_option = state_option
        
    def elevator(self):
        self.state_option.state()

#stuck = Elevator(ElevStuck())
#stuck.elevator()

"""Falta obter resultado que o elevador está stuck, exemplo retornar um booleano 1 para stuck na função elevador"""
"""Depois passar esse boleano para a if name main em Teams Observer"""