class Person():

    def __init__(self, name, last_name, email) -> None:
        self.name = name
        self.last_name = last_name
        self.email = email

    def toString(self):
        print("Nome: {}\nSobrenome: {}\nEmail: {}".format(self.name, self.last_name, self.email))
