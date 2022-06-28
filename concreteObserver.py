from observer import Observer
from concreteSubject import ConcreteSubject

class MessageObserverOne(Observer):
    def update(self, elev, message, people):
        if message == 'stuck':
            print(f'Message to maitenance and security teams: {elev} elevator is {message}.')

class MessageObserverTwo(Observer):
    def update(self, elev, message, people):
        if message == 'maintenance':
            if elev == 'social':
                print(f'Speedup service elevator.')
            elif elev == 'Service':
                print(f'Speedup social elevator.')

class MessageObserverThree(Observer):
    def update(self, elev, message, people):
        if message == 'stuck' and people == True:
            print(f'Message to passangers: maintenance and security teams are on their way.')
            print(f'Start playing loung music on {elev} elevator.')

class MessageObserverFourth(Observer):
    def update(self, elev, message, people):
        if message == 'normal':
            print(f'The {elev} elevator is working properly.')

def main():
    subject = ConcreteSubject()

    message_one = MessageObserverOne()
    message_two = MessageObserverTwo()
    message_three = MessageObserverThree()
    message_Fourth = MessageObserverFourth()

    subject.attach(message_one)
    subject.attach(message_two)
    subject.attach(message_three)
    subject.attach(message_Fourth)

    subject.notify('social', 'stuck', True)

if __name__ == '__main__':
    main()