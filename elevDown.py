from elevState import ElevState

class ElevDown(ElevState):
    def __init__(self):
        self.do = 'going down'

    def state(self):
        print(f'Elevator is {self.do}.')

#ElevDown().state()