class Produto:
    def __init__(self, id, nome, codigoBarras, preco, quantidade):
        self.id = id
        self.nome = nome
        self.codigoBarras = codigoBarras
        self.preco = preco
        self.quantidade = quantidade

    def get_info(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "codigoBarras": self.codigoBarras,
            "preco": self.preco,
            "quantidade": self.quantidade
        }