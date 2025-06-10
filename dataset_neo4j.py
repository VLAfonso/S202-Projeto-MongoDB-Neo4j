from funcionarios_crud import FuncionariosCRUD

class Dataset:
    def __init__(self, database):
        self.funcionarios = FuncionariosCRUD(database)
    
    def insert_dataset(self):
        # Adicionar funcionários
        self.funcionarios.criar_funcionario("Ana Clara", "01/03/2001", "023.823.766-34", 0, "(11) 99890-0143", "ana_clara@hotmail.com")
        self.funcionarios.criar_funcionario("Brenda", "04/04/2001", "125.765.932-81", 1, "(35) 99876-0923", "brenda@gmail.com")
        self.funcionarios.criar_funcionario("Carlos Daniel", "12/07/2002", "044.346.123-67", 2, "(35) 99874-1230", "carlos_daniel@hotmail.com")
        self.funcionarios.criar_funcionario("Fernanda", "03/04/1990", "768.223.465-90", 3, "(35) 99889-1254", "fernanda@gmail.com")
        self.funcionarios.criar_funcionario("Júlio César", "23/12/1987", "458.124.58-78", 4, "(35) 99985-5372", "julio_cesar@hotmail.com")
        self.funcionarios.criar_funcionario("Maria Eduarda", "30/08/1999", "357.632.558-74", 5, "(35) 98845-6106", "maria_eduarda@hotmail.com")
        self.funcionarios.criar_funcionario("Otávio", "31/07/1995", "286.457.147-99", 6, "(35) 99980-6523", "otavio@hotmail.com")
        self.funcionarios.criar_funcionario("Pedro Henrique", "22/06/2003", "231.672.366-64", 7, "(35) 99887-7678", "pedro_henrique@gmail.com")
        self.funcionarios.criar_funcionario("Rafaela", "29/05/2002", "155.313.789-72", 8, "(35) 99878-2231", "rafaela@gmail.com")
        self.funcionarios.criar_funcionario("Valdecir", "17/11/1976", "873.231.678-25", 9, "(35) 99980-0135", "valdecir@hotmail.com")

        # Adicionar setores
        self.funcionarios.criar_setor("Recursos Humanos", 0)
        self.funcionarios.criar_setor("Padaria", 1)
        self.funcionarios.criar_setor("Açougue", 2)
        self.funcionarios.criar_setor("Caixa", 3)
        self.funcionarios.criar_setor("Estoque", 4)

        # Relacionar funcionários a seu setor
        self.funcionarios.funcionario_setor("Fernanda", "Recursos Humanos")
        self.funcionarios.funcionario_setor("Júlio César", "Padaria")
        self.funcionarios.funcionario_setor("Rafaela", "Padaria")       
        self.funcionarios.funcionario_setor("Otávio", "Açougue")
        self.funcionarios.funcionario_setor("Valdecir", "Açougue")
        self.funcionarios.funcionario_setor("Ana Clara", "Caixa")
        self.funcionarios.funcionario_setor("Maria Eduarda", "Caixa")
        self.funcionarios.funcionario_setor("Pedro Henrique", "Caixa")
        self.funcionarios.funcionario_setor("Brenda", "Estoque")
        self.funcionarios.funcionario_setor("Carlos Daniel", "Estoque")

        # Relacionar gerentes a seus funcionarios
        self.funcionarios.funcionario_gerente("Rafaela", "Júlio César")
        self.funcionarios.funcionario_gerente("Otávio", "Valdecir")
        self.funcionarios.funcionario_gerente("Ana Clara", "Maria Eduarda")
        self.funcionarios.funcionario_gerente("Pedro Henrique", "Maria Eduarda")
        self.funcionarios.funcionario_gerente("Brenda", "Carlos Daniel")
