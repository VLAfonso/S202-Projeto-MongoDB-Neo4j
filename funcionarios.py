class FuncionariosCRUD:
    def __init__(self, database):
        self.db = database

    def criar_funcionario(self, nome, dataNascimento, cpf, id, telefone, email):
        query = "CREATE (:Funcionario {nome: $nome, dataNascimento: $dataNascimento, cpf: $cpf, id: $id, telefone: $telefone, email: $email})"
        result = self.db.execute_query(query, {'nome': nome, 'dataNascimento': dataNascimento, 'cpf': cpf, 'id': id, 'telefone': telefone, 'email': email})
        if result is not None:
            print(f'O funcionario {nome} foi criado no banco de dados')
    
    def ler_funcionario(self, id):
        query = "MATCH (f:Funcionario {id: $id}) RETURN f.nome as nome, f.dataNascimento as dataNascimento, f.cpf as cpf, f.telefone as telefone, f.email as email"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {
                "nome": result["nome"],
                "dataNascimento": result["dataNascimento"],
                "cpf": result["cpf"],
                "telefone": result["telefone"],
                "email": result["email"]
            }
        return None
    
    def atualizar_funcionario(self, id, telefone, email):
        query = "MATCH (f:Funcionario {id: $id}) SET f.telefone = $telefone, f.email = $email"
        result = self.db.execute_query(query, {'id': id, 'telefone': telefone, 'email': email})
        if result is not None:
            print(f'O funcionario com id: {id} foi alterado, novo telefone: {telefone} e novo email: {email}')
    
    def apagar_funcionario(self, id):
        query = "MATCH (f:Funcionario {id: $id}) DETACH DELETE f"
        result = self.db.execute_query(query, {'id': id})
        if result is not None:
            print(f'O funcionario com id: {id} foi deletado do banco de dados')

    def criar_setor(self, nome, id):
        query = "CREATE (:Setor {id: $id, nome: $nome})"
        result = self.db.execute_query(query, {'id': id, 'nome': nome})
        if result is not None:
            print(f'O setor {nome} foi criado no banco de dados')
    
    def ler_setor(self, id):
        query = "MATCH (s:Setor {id: $id}) RETURN f.nome as nome"
        parameters = {"id": id}
        results = self.db.execute_query(query, parameters)
        if results:
            result = results[0]
            return {
                "nome": result["nome"]
            }
        return None
    
    def atualizar_setor(self, id, nome):
        query = "MATCH (s:Setor {id: $id}) SET s.nome = $nome"
        result = self.db.execute_query(query, {'id': id, 'nome': nome})
        if result is not None:
            print(f'O setor com id: {id} foi alterado, novo nome: {nome}')
    
    def apagar_setor(self, id):
        query = "MATCH (s:Setor {id: $id}) DETACH DELETE s"
        result = self.db.execute_query(query, {'id': id})
        if result is not None:
            print(f'O setor com id: {id} foi deletado do banco de dados')