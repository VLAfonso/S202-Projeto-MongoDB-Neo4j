from cli import InicialCLI, EstoqueCLI, FuncionariosCLI
from database_mongodb import DatabaseMongoDB
from database_neo4j import DatabaseNeo4j
from funcionarios import FuncionariosCRUD
from estoque import EstoqueCRUD

# Criar banco de dados do estoque
dbMongoDB = DatabaseMongoDB(database='Supermercado', collection='Estoque')
dbMongoDB.resetDatabase()

# Criar banco de dados dos funcionários e setores
dbNeo4j = DatabaseNeo4j("neo4j://localhost:7687", "neo4j", "neo4jneo4j")
dbNeo4j.insert_dataset()

# Criar instância do CRUD de estoque, funcionários e setores
estoque_crud = EstoqueCRUD(dbMongoDB)
funcionarios_crud = FuncionariosCRUD(dbNeo4j)

# Criar e iniciar CLI
cli = InicialCLI(estoque_crud, funcionarios_crud)
cli.run()