from produtos import Produto
from pymongo import MongoClient
from bson.objectid import ObjectId

class EstoqueCRUD:
    def __init__(self, database):
        self.db = database
        self.collection = self.db['produtos']

    def criar_produto(self, produto : Produto):
        try:
            res = self.collection.insert_one(produto.get_info())
            print(f"Produto criado com id: {res.inserted_id}")
            return str(res.inserted_id)
        except Exception as e:
            print(f"Erro ao criar produto: {e}")
            return None
    
    def ler_produto_by_id(self, id):
        try:
            res = self.collection.find_one({"_id": ObjectId(id)})
            if res:
                print(f"Produto encontrado: {res}")
            else:
                print("Produto não encontrado.")
            return res
        except Exception as e:
            print(f"Erro ao ler produto: {e}")
            return None
    
    def atualizar_produto(self, id, preco, quantidade):
        try:
            res = self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"preco": preco, "quantidade": quantidade}}
            )
            print(f"{res.modified_count} produto(s) atualizado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            return None
        
    def apagar_produto(self, id):
        try:
            res = self.collection.delete_one({"_id": ObjectId(id)})
            print(f"{res.deleted_count} produto(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            return None