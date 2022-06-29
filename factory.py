from abc import ABC, abstractmethod
from elevator import Elevator
from elevUp import ElevUp
from elevDown import ElevDown
from elevStop import ElevStop
from elevStuck import ElevStuck
from elevIdle import ElevIdle
from concreteSubject import ConcreteSubject
from concreteObserver import MessageObserverOne, MessageObserverThree, MessageObserverTwo, MessageObserverFourth

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

class ServiceElevFactory(ElevFactory):
    def __init__(self, state_option):
        self.state_option = state_option
    def createElev(self):
        return ServiceElevator(self.state_option)

class IElevators(ABC):
    @abstractmethod
    def move(self):
        pass

class SocialElevator(IElevators):
    def __init__(self, state_option):
        self.state_option = state_option

    def move(self):
        
        subject = ConcreteSubject()
        if self.state_option == 'stuck':
            result = Elevator(ElevStuck())
            result.elevator()
            message_one = MessageObserverOne()
            message_three = MessageObserverThree()
            subject.attach(message_one)
            subject.attach(message_three)
            subject.notify(el, st, fe)
        elif self.state_option == 'up':
            result = Elevator(ElevUp())
            result.elevator()
            message_Fourth = MessageObserverFourth()
            subject.attach(message_Fourth)
            subject.notify(el, st, fe)
        elif self.state_option == 'down':
            result = Elevator(ElevDown())
            result.elevator()
            message_Fourth = MessageObserverFourth()
            subject.attach(message_Fourth)
            subject.notify(el, st, fe)
        elif self.state_option == 'stop':
            result = Elevator(ElevStop())
            result.elevator()
            message_Fourth = MessageObserverFourth()
            subject.attach(message_Fourth)
            subject.notify(el, st, fe)
        elif self.state_option == 'idle':
            result = Elevator(ElevIdle())
            result.elevator()
            message_two = MessageObserverTwo()
            subject.attach(message_two)
            #If idle, elevator is considered empty
            subject.notify(el, st, False)

class ServiceElevator(IElevators):
    def __init__(self, state_option):
        self.state_option = state_option

    def move(self):
        
        subject = ConcreteSubject()
        if self.state_option == 'stuck':
            result = Elevator(ElevStuck())
            result.elevator()
            message_one = MessageObserverOne()
            message_three = MessageObserverThree()
            subject.attach(message_one)
            subject.attach(message_three)
            subject.notify(el, st, fe)
        elif self.state_option == 'up':
            result = Elevator(ElevUp())
            result.elevator()
            message_Fourth = MessageObserverFourth()
            subject.attach(message_Fourth)
            subject.notify(el, st, fe)
        elif self.state_option == 'down':
            result = Elevator(ElevDown())
            result.elevator()
            message_Fourth = MessageObserverFourth()
            subject.attach(message_Fourth)
            subject.notify(el, st, fe)
        elif self.state_option == 'stop':
            result = Elevator(ElevStop())
            result.elevator()
            message_Fourth = MessageObserverFourth()
            subject.attach(message_Fourth)
            subject.notify(el, st, fe)
        elif self.state_option == 'idle':
            result = Elevator(ElevIdle())
            result.elevator()
            message_two = MessageObserverTwo()
            subject.attach(message_two)
            #If idle, elevator is considered empty
            subject.notify(el, st, False)        

def client_code(elev: ElevFactory):
    elev.planMove()

if __name__ == '__main__':
    
    el = input('social or service: ').lower()
    st = input('Elevator state (stuck, up, down, stop or idle):').lower()
    fe = input('Full or empty (True or False): ')
    if fe == 'True' or fe == 'true':
        fe = bool(fe)
    else:
        fe = bool('')
    
    print('')
    if el == 'social':
        client_code(SocialElevFactory(st))
    elif el == 'service':
        client_code(ServiceElevFactory(st))