from elevState import ElevState

class ElevIdle(ElevState):
    def __init__(self):
        self.do = 'idle'

    def state(self):
        print(f'Elevator is {self.do}.')

#ElevIdle().state()