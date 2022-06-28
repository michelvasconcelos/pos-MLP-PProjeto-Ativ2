from elevState import ElevState

class ElevStuck(ElevState):
    def __init__(self):
        self.do = 'stuck'
        self.stuck = True

    def state(self):
        print(f'Elevator is {self.do}.')

#ElevStuck().state()