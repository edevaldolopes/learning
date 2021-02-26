from datetime import datetime


class People:
    currentYear = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def start_eat(self, food):
        if self.eating:
            print(f'{self.name} are eat.')
            return
        if self.talking:
            print(f'{self.name} not eating speak.')
            return
        print(f'{self.name} are eat {food}.')
        self.eating = True

    def end_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return
        print(f'{self.name} stopped eating.')
        self.eating = False

    def start_speak(self, topic):
        if self.eating:
            print(f'{self.name} not speak eating.')
            return
        if self.talking:
            print(f'{self.name} is talking {topic}.')
            return
        print(f'{self.name} is talking {topic}.')
        self.talking = True

    def end_speak(self):
        if not self.talking:
            print(f'{self.name} is not talking.')
            return
        print(f'{self.name} stopped speak.')
        self.talking = False

    def birthYear(self):
        birthday = self.currentYear - (self.age + 1)
        print(f'{self.name} is {birthday}')


p1 = People('anna', 5)
p1.birthYear()
p1.start_speak('python oo')
p1.start_eat('orange')
