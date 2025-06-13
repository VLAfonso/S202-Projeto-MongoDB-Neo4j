from funcionario import Funcionario
from setor import Setor

class FuncionariosCRUD:
    def __init__(self, database):
        self.db = database

    # CRUD do funcionário
    def criar_funcionario(self, funcionario: Funcionario):
        query = "CREATE (:Funcionario {nome: $nome, dataNascimento: $dataNascimento, cpf: $cpf, id: $id, telefone: $telefone, email: $email})"
        result = self.db.execute_query(query, funcionario.get_info())
        if result is not None:
            print(f'O funcionário {funcionario.nome} foi criado no banco de dados')
        else:
            print('Não foi possível criar o funcionário.')
    
    def ler_todos_funcionarios(self):
        query = "MATCH (f:Funcionario) RETURN f.nome as nome, f.dataNascimento as dataNascimento, f.cpf as cpf, f.telefone as telefone, f.email as email"
        results_funcionario = self.db.execute_query(query)

        query2 = "MATCH (f:Funcionario)-[:TRABALHA_EM]->(s:Setor) RETURN f.nome AS nome_funcionario, s.nome AS nome_setor"
        results_setor = self.db.execute_query(query2)

        query3 = "MATCH (g:Funcionario)-[:GERENCIA]->(f:Funcionario) RETURN g.nome AS nome_gerente, f.nome AS nome_funcionario"
        results_gerente = self.db.execute_query(query3)

        if results_funcionario:
            for result in results_funcionario:
                print("-" * 40)
                print(f"Nome: {result['nome']}")
                print(f"Data de nascimento: {result['dataNascimento']}")
                print(f"CPF: {result['cpf']}")
                print(f"Telefone: {result['telefone']}")
                print(f"Email: {result['email']}")
                for result2 in results_setor:
                    if result['nome']==result2['nome_funcionario']:
                        print(f"Setor: {result2['nome_setor']}")
                for result3 in results_gerente:
                    if result['nome']==result3['nome_funcionario']:
                        print(f"Gerente: {result3['nome_gerente']}")
        else:
            print('Não há funcionários cadastrados.')
    
    def atualizar_funcionario(self, id, telefone, email):
        query = "MATCH (f:Funcionario {id: $id}) SET f.telefone = $telefone, f.email = $email"
        result = self.db.execute_query(query, {'id': id, 'telefone': telefone, 'email': email})
        if result is not None:
            print(f'O funcionário com id: {id} foi alterado, novo telefone: {telefone} e novo email: {email}')
        else:
            print('Não foi possível atualizar o funcionário.')
    
    def apagar_funcionario(self, id):
        query = "MATCH (f:Funcionario {id: $id}) DETACH DELETE f"
        result = self.db.execute_query(query, {'id': id})
        if result is not None:
            print(f'O funcionário com id: {id} foi deletado do banco de dados')
        else:
            print('Não foi possível apagar o funcionário.')

    # CRUD do setor
    def criar_setor(self, setor: Setor):
        query = "CREATE (:Setor {id: $id, nome: $nome})"
        result = self.db.execute_query(query, setor.get_info())
        if result is not None:
            print(f'O setor {setor.nome} foi criado no banco de dados')
        else:
            print('Não foi possível criar o setor.')
    
    def ler_todos_setores(self):
        query = "MATCH (s:Setor) RETURN s.nome as nome"
        results_setor = self.db.execute_query(query)

        query2 = "MATCH (f:Funcionario)-[:TRABALHA_EM]->(s:Setor) RETURN f.nome AS nome_funcionario, s.nome AS nome_setor"
        results_funcionarios = self.db.execute_query(query2)

        if results_setor:
            for result in results_setor:
                print("-" * 40)
                print(f"Nome: {result['nome']}")
                funcionarios = []
                for result2 in results_funcionarios:
                    if result['nome']==result2['nome_setor']:
                        funcionarios.append({'nome':result2['nome_funcionario']})
                if funcionarios != []:
                    print("Funcionários:")
                    for funcionario in funcionarios:
                        print(f"     Nome: {funcionario['nome']}")
        else:
            print('Não há setores cadastrados.')
    
    def atualizar_setor(self, id, nome):
        query = "MATCH (s:Setor {id: $id}) SET s.nome = $nome"
        result = self.db.execute_query(query, {'id': id, 'nome': nome})
        if result is not None:
            print(f'O setor com id: {id} foi alterado, novo nome: {nome}')
        else:
            print('Não foi possível alterar o setor.')
    
    def apagar_setor(self, id):
        query = "MATCH (s:Setor {id: $id}) DETACH DELETE s"
        result = self.db.execute_query(query, {'id': id})
        if result is not None:
            print(f'O setor com id: {id} foi apagado do banco de dados')
        else:
            print('Não foi possível apagar o setor.')

    # Relacionar setor e funcionário
    def funcionario_setor(self, funcionario, setor):
        query = "MATCH (f:Funcionario {nome: $nome_funcionario}), (s:Setor {nome: $nome_setor}) CREATE (f)-[:TRABALHA_EM]->(s)"
        result = self.db.execute_query(query, {'nome_funcionario': funcionario, 'nome_setor': setor})
        if result is not None:
            print(f'O relacionamento entre o funcionário {funcionario} e o setor {setor} foi criado no banco de dados')

    # Relacionar funcionário e gerente
    def funcionario_gerente(self, funcionario, gerente):
        query = "MATCH (f:Funcionario {nome: $nome_funcionario}), (g:Funcionario {nome: $nome_gerente}) CREATE (g)-[:GERENCIA]->(f)"
        result = self.db.execute_query(query, {'nome_funcionario': funcionario, 'nome_gerente': gerente})
        if result is not None:
            print(f'O relacionamento entre o gerente {gerente} e o funcionário {funcionario} foi criado no banco de dados')