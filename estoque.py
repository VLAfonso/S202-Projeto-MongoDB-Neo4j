class EstoqueCRUD:
    def __init__(self, database):
        self.db = database

    def criar_produto(self, nome, codigoBarras, id, preco, quantidade):
        query = "CREATE (:Produto {nome: $nome, codigoBarras: $codigoBarras, id: $id, preco: $preco, quantidade: $quantidade})"
        result = self.db.execute_query(query, {'nome': nome, 'codigoBarras': codigoBarras, 'id': id, 'preco': preco, 'quantidade': quantidade})
        if result is not None:
            print(f'O produto {nome} foi criado no banco de dados')
    
    def ler_produto_by_id(self, id):
        query = "MATCH (p:Produto {id: $id}) RETURN p.nome as nome, p.codigoBarras as codigoBarras, p.preco as preco, p.quantidade as quantidade"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"], result["codigoBarras"] ,result["preco"], result["quantidade"]) for result in results]
    
    def atualizar_produto(self, id, preco, quantidade):
        query = "MATCH (p.Produto {id: $id}) SET p.preco = $preco, p.quantidade = $quantidade"
        result = self.db.execute_query(query, {'id': id, 'preco': preco, 'quantidade': quantidade})
        if result is not None:
            print(f'O produto com id: {id} foi alterado, novo preco: {preco} e nova quantidade: {quantidade}')
    
    def apagar_produto(self, id):
        query = "MATCH (p:Produto {id: $id}) DETACH DELETE p"
        result = self.db.execute_query(query, {'id': id})
        if result is not None:
            print(f'O produto com id: {id} foi deletado do banco de dados')