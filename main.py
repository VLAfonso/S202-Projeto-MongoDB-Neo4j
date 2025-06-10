from cli import InicialCLI, EstoqueCLI, FuncionariosCLI
from database_mongodb import DatabaseMongoDB
from database_neo4j import DatabaseNeo4j
from funcionarios import FuncionariosCRUD

#dbMongo = DatabaseMongoDB("Supermercado", "Estoque")
dbNeo4j = DatabaseNeo4j("neo4j://localhost:7687", "neo4j", "neo4jneo4j")
# dbNeo4j.insert_dataset()

funcionarios_crud = FuncionariosCRUD(dbNeo4j)
# estoque_crud = EstoqueCRUD(dbMongo)

cli = InicialCLI("estoque", funcionarios_crud)

cli.run()