from estoque import EstoqueCRUD
from funcionarios import FuncionariosCRUD

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "sair":
                print("Até mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class InicialCLI(SimpleCLI):
    def __init__(self, estoque, funcionarios):
        super().__init__()
        self.estoque_cli = EstoqueCLI(estoque)
        self.funcionario_cli = FuncionariosCLI(funcionarios)
        self.add_command("1", self.estoque_cli.run)
        self.add_command("2", self.funcionario_cli.run)

    def run(self):
        print("Bem-vindo ao Sistema de Gerenciamento do Supermercado!")
        print("O que deseja acessar?")
        print("     1- Controle de estoque;")
        print("     2- Gerência de funcionários e setores;")
        print("Digite 'sair' para encerrar.")
        super().run()
        

class EstoqueCLI(SimpleCLI):
    def __init__(self, estoque: EstoqueCRUD):
        super().__init__()
        self.estoque = estoque
        self.add_command("1", self.criar_produto)
        self.add_command("2", self.ler_produto)
        self.add_command("3", self.atualizar_produto)
        self.add_command("4", self.apagar_produto)

    def criar_produto(self):
        id = input("Entre com o id: ")
        nome = input("Entre com o nome: ")
        codigoBarras = int(input("Entre com o codigoBarras: "))
        preco = float(input("Entre com o preco: "))
        quantidade = int(input("Entre com a quantidade: "))
        self.estoque.criar_produto(nome, codigoBarras, id, preco, quantidade)

    def ler_produto(self):
        id = int(input("Entre com o id: "))
        produto = self.estoque.ler_produto_by_id(id)
        if produto:
            print(f"Nome: {produto['nome']}")
            print(f"Codigo de barras: {produto['codigoBarras']}")
            print(f"Preco: {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")

    def atualizar_produto(self):
        nome = input("Entre com o novo nome: ")
        codigoBarras = int(input("Entre com o novo codigo de barras: "))
        preco = float(input("Entre com o novo preco: "))
        quantidade = int(input("Entre com a nova quantidade: "))
        self.estoque.atualizar_produto(nome, codigoBarras, preco, quantidade)

    def apagar_produto(self):
        id = int(input("Entre com o id: "))
        self.estoque.apagar_produto(id)
        
    def run(self):
        print("-"*75)
        print("Bem-vindo ao controle de estoque!")
        print("O que deseja acessar:")
        print("     1- Adicionar produto;")
        print("     2- Listar produtos;")
        print("     3- Atualizar produto;")
        print("     4- Apagar produto;")
        print("Digite 'sair' para encerrar.") 
        super().run()
        # Indicar que voltou ao menu
        print("-"*75)
        print("Bem-vindo ao Sistema de Gerenciamento do Supermercado!")
        print("O que deseja acessar:")
        print("     1- Controle de estoque;")
        print("     2- Gerência de funcionários e setores;")
        print("Digite 'sair' para encerrar.")  


class FuncionariosCLI(SimpleCLI):
    def __init__(self, funcionarios: FuncionariosCRUD):
        super().__init__()
        self.funcionarios = funcionarios
        self.add_command("1", self.criar_funcionario)
        self.add_command("2", self.ler_funcionario)
        self.add_command("3", self.atualizar_funcionario)
        self.add_command("4", self.apagar_funcionario)
        self.add_command("5", self.criar_setor)
        self.add_command("6", self.ler_setor)
        self.add_command("7", self.atualizar_setor)
        self.add_command("8", self.apagar_setor)
        self.add_command("9", self.funcionario_setor)
        self.add_command("10", self.funcionario_gerente)


    def criar_funcionario(self):
        id = int(input("Entre com o id: "))
        nome = input("Entre com o nome: ")
        dataNascimento = input("Entre com a data de nascimento: ")
        cpf = input("Entre com o cpf: ")
        telefone = input("Entre com o telefone: ")
        email = input("Entre com o email: ")
        self.funcionarios.criar_funcionario(nome, dataNascimento, cpf, id, telefone, email)

    def ler_funcionario(self):
        id = int(input("Entre com o id: "))
        funcionario = self.funcionarios.ler_funcionario(id)
        if funcionario:
            print(f"Nome: {funcionario['nome']}")
            print(f"Data de nascimento: {funcionario['dataNascimento']}")
            print(f"CPF: {funcionario['cpf']}")
            print(f"Telefone: {funcionario['telefone']}")
            print(f"Email: {funcionario['email']}")

    def atualizar_funcionario(self):
        id = int(input("Entre com o id: "))
        telefone = input("Entre com o novo telefone: ")
        email = input("Entre com o novo email: ")
        self.funcionarios.atualizar_funcionario(id, telefone, email)

    def apagar_funcionario(self):
        id = int(input("Entre com o id: "))
        self.funcionarios.apagar_funcionario(id)

    def criar_setor(self):
        '''
        id = int(input("Enter the id: "))
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        price = float(input("Enter the price: "))
        self.funcionarios.criar_funcionario(id, title, author, year, price)
        '''

    def ler_setor(self):
        '''
        id = int(input("Enter the id: "))
        funcionario = self.funcionario.ler_funcionario_by_id(id)
        if funcionario:
            print(f"Title: {funcionario['titulo']}")
            print(f"Author: {funcionario['autor']}")
            print(f"Year: {funcionario['ano']}")
            print(f"Price: {funcionario['preco']}")
            '''

    def atualizar_setor(self):
        '''
        id = int(input("Enter the id: "))
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        year = int(input("Enter the new year: "))
        price = float(input("Enter the new price: "))
        self.funcionarios.atualizar_funcionario(id, title, author, year, price)
        '''

    def apagar_setor(self):
        '''
        id = int(input("Enter the id: "))
        self.funcionarios.apagar_funcionario(id)
        '''
    def funcionario_setor(self):
        '''
        Ler nome do funcionário e setor e criar relacionamento entre eles
        '''
    
    def funcionario_gerente(self):
        '''
        Ler nome do funcionário e gerente e criar relacionamento entre eles
        '''
        
    def run(self):
        print("-"*75)
        print("Bem-vindo ao controle de funcionários!")
        print("O que deseja acessar:")
        print("     1- Cadastrar funcionário;")
        print("     2- Listar funcionários;")
        print("     3- Atualizar dados de um funcionário;")
        print("     4- Apagar funcionário;")
        print("     5- Cadastrar setor;")
        print("     6- Listar setores;")
        print("     7- Atualizar dados de um setor;")
        print("     8- Apagar setor;")
        print("     9- Cadastrar funcionário em um setor;")
        print("     10- Cadastrar gerente de um funcionario;")
        print("Digite 'sair' para encerrar.") 
        super().run()
        # Indicar que voltou ao menu
        print("-"*75)
        print("Bem-vindo ao Sistema de Gerenciamento do Supermercado!")
        print("O que deseja acessar:")
        print("     1- Controle de estoque;")
        print("     2- Gerência de funcionários e setores;")
        print("Digite 'sair' para encerrar.") 