from neo4j import GraphDatabase
from dataset_neo4j import Dataset

class DatabaseNeo4j:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.dataset = Dataset(self)

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:  
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data
        
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
    
    def insert_dataset(self):
        # Apagar todos os dados
        self.drop_all()
        # Inserir dados base do banco
        self.dataset.insert_dataset()