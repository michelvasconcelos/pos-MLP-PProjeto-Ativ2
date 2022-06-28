from elevState import ElevState

class ElevUp(ElevState):
    def __init__(self):
        self.do = 'going up'

    def state(self):
        print(f'Elevator is {self.do}.')

#ElevUp().state()