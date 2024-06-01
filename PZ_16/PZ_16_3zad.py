class Person:
    count = 0
    def __init__(self, age):
        self.age = age
        Person.count += 1

    @staticmethod
    def static():
        print(f'Создано экземпляров класса: {Person.count}')

e1 = Person('20')
e2 = Person('2020')

Person.static()

