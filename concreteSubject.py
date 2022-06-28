from subject import Subject

class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def notify(self, elev, message, people):
        for observer in self._observers:
            observer.update(elev, message, people)