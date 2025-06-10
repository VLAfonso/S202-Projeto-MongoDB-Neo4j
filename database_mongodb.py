from typing import Collection
import pymongo
from dataset_mongodb import dataset
import json

class DatabaseMongoDB:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection.name)
            self.db.create_collection(self.collection.name)  # recria antes de aplicar schema
            self.collection = self.db[self.collection.name]

            # Aplicar novamente o schema após recriar
            with open("schema.json", "r") as f:
                schema = json.load(f)

            self.db.command({
                "collMod": self.collection.name,
                "validator": schema,
                "validationLevel": "strict",
                "validationAction": "error"
            })

            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)
