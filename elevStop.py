from elevState import ElevState

class ElevStop(ElevState):
    def __init__(self):
        self.do = 'stopped'

    def state(self):
        print(f'Elevator is {self.do}.')

#ElevStop().state()