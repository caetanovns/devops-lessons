'''pacote person'''


class Person():
    """Classe person"""

    def __init__(self, name, last_name, email) -> None:
        '''Construtor da classe'''
        self.name = name
        self.last_name = last_name
        self.email = email

    def to_string(self):
        '''Método para retornar person em string'''
        print(
            f"Nome: {self.name}\nSobrenome: {self.last_name}\nEmail: {self.email}")

    def pub2(self):
        '''Novo metodo'''
