class Setor:
    def __init__(self, nome, id):
        self.id = id
        self.nome = nome

    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }