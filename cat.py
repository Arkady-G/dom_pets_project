class Cats:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getname(self):
        return self.name

    def getgender(self):
        return self.gender

    def getage(self):
        return self.age

    def print_list(self):
        print('Имя - {}'.format(self.name))
        print('Пол - {}'.format(self.gender))
        print('Возраст - {}\n'.format(self.age))