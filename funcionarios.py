class FuncionariosCRUD:
    def __init__(self, database):
        self.db = database

    def criar_funcionario(self, nome, dataNascimento, cpf, id, telefone, email):
        query = "CREATE (:Funcionario {nome: $nome, dataNascimento: $dataNascimento, cpf: $cpf, id: $id, telefone: $telefone, email:$email})"
        result = self.db.execute_query(query, {'nome': nome, 'dataNascimento': dataNascimento, 'cpf': cpf, 'id': id, 'telefone': telefone, 'email': email})
        if result is not None:
            print(f'O produto {nome} foi criado no banco de dados')
    
    def ler_funcionario(self, id):
        query = "MATCH (f:Funcionario {id: $id}) RETURN f.nome as nome, f.dataNascimento as dataNascimento, f.cpf as cpf, f.telefone as telefone, f.email as email"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        return [(result["nome"], result["dataNascimento"], result["cpf"] ,result["telefone"], result["email"]) for result in results]
    
    def atualizar_funcionario(self, id, telefone, email):
        query = "MATCH (f.Funcionario {id: $id}) SET f.telefone = $telefone, f.email = $email"
        result = self.db.execute_query(query, {'id': id, 'telefone': telefone, 'email': email})
        if result is not None:
            print(f'O funcionario com id: {id} foi alterado, novo telefone: {telefone} e novo email: {email}')
    
    def apagar_funcionario(self, id):
        query = "MATCH (f:Funcionario {id: $id}) DETACH DELETE f"
        result = self.db.execute_query(query, {'id': id})
        if result is not None:
            print(f'O funcionario com id: {id} foi deletado do banco de dados')