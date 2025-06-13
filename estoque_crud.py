from produtos import Produto
from pymongo import MongoClient
from bson.objectid import ObjectId

class EstoqueCRUD:
    def __init__(self, database):
        self.db = database

    def criar_produto(self, produto : Produto):
        try:
            res = self.db.collection.insert_one(produto.get_info())
            print(f"Produto {produto.nome} criado.")
            return str(res.inserted_id)
        except Exception as e:
            print(f"Erro ao criar produto: {e}")
            return None
    
    def ler_todos_produtos(self):
        try:
            resultados = self.db.collection.find()
            produtos = list(resultados)
            if produtos:
                for produto in produtos:
                    print("-" * 40)
                    print(f"Nome: {produto.get('nome', 'N/A')}")
                    print(f"Código de barras: {produto.get('codigoBarras', 'N/A')}")
                    print(f"Preço: {produto.get('preco', 'N/A')}")
                    print(f"Quantidade: {produto.get('quantidade', 'N/A')}")
            else:
                print("Nenhum produto cadastrado.")
            return produtos
        except Exception as e:
            print(f"Erro ao ler produtos: {e}")
            return []

    
    def atualizar_produto(self, id, preco, quantidade):
        try:
            res = self.db.collection.update_one(
                {"id": id},
                {"$set": {"preco": preco, "quantidade": quantidade}}
            )
            print(f"{res.modified_count} produto(s) atualizado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            return None
        
    def apagar_produto(self, id):
        try:
            res = self.db.collection.delete_one({"id": id})
            print(f"{res.deleted_count} produto(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            return None