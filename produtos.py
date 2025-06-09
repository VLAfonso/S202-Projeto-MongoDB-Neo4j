class Produto:
    def __init__(self, nome, id, codigoBarras, preco, quantidade):
        self.nome = nome
        self.id = id
        self.codigoBarras = codigoBarras
        self.preco = preco
        self.quantidade = quantidade

    def get_info(self):
        return {
            "nome": self.nome,
            "id": self.id,
            "codigoBarras": self.codigoBarras,
            "preco": self.preco,
            "quantidade": self.quantidade
        }