from abc import ABC, abstractmethod
from elevator import Elevator
from elevUp import ElevUp
from elevDown import ElevDown
from elevStop import ElevStop
from elevStuck import ElevStuck
from elevIdle import ElevIdle

class ElevFactory(ABC):
    @abstractmethod
    def createElev(self):
        pass

    def planMove(self):
        pMove = self.createElev()
        result = f'{pMove.move()}'
        return result

class SocialElevFactory(ElevFactory):
    def __init__(self, state_option):
        self.state_option = state_option
    def createElev(self):
        return SocialElevator(self.state_option)

class IElevators(ABC):
    @abstractmethod
    def move(self):
        pass

class SocialElevator(IElevators):
    def __init__(self, state_option):
        self.state_option = state_option
        #self.category = 'social'

    def move(self):
        #result = (f'{self.category} elevator is {self.state_option}')
        if self.state_option == 'stuck':
            res = Elevator(ElevStuck())
            res.elevator() #result = res.elevator()
        elif self.state_option == 'up':
            res = Elevator(ElevUp())
            res.elevator()
        elif self.state_option == 'down':
            res = Elevator(ElevDown())
            res.elevator()
        elif self.state_option == 'stop':
            res = Elevator(ElevStop())
            res.elevator()
        elif self.state_option == 'idle':
            res = Elevator(ElevIdle())
            res.elevator()
        #return result

def client_code(elev: ElevFactory):
    elev.planMove()

if __name__ == '__main__':
    client_code(SocialElevFactory('stuck'))
    client_code(SocialElevFactory('up'))
    client_code(SocialElevFactory('down'))
    client_code(SocialElevFactory('stop'))
    client_code(SocialElevFactory('idle'))