class Funcionario:
    def __init__(self, nome, dataNascimento, cpf, id, telefone, email):
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "dataNascimento": self.dataNascimento,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email
        }