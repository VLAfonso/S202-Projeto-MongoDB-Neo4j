from estoque_crud import EstoqueCRUD
from funcionarios_crud import FuncionariosCRUD
from produtos import Produto
from funcionario import Funcionario
from setor import Setor

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
        print("-"*75)
        print("Bem-vindo ao Sistema de Gerenciamento do Supermercado!")
        print("O que deseja acessar?")
        print("     1- Controle de estoque;")
        print("     2- Gerência de funcionários e setores;")
        print("Digite 'sair' para encerrar.")
        super().run()
        
# CLI para gerência do estoque (produtos)
class EstoqueCLI(SimpleCLI):
    def __init__(self, estoque: EstoqueCRUD):
        super().__init__()
        self.estoque = estoque
        self.add_command("1", self.criar_produto)
        self.add_command("2", self.ler_produto)
        self.add_command("3", self.atualizar_produto)
        self.add_command("4", self.apagar_produto)

    def criar_produto(self):
        id = int(input("Entre com o id: "))
        nome = input("Entre com o nome: ")
        codigoBarras = int(input("Entre com o código de barras: "))
        preco = float(input("Entre com o preço: "))
        quantidade = int(input("Entre com a quantidade: "))
        produto = Produto(id, nome, codigoBarras, preco, quantidade)
        self.estoque.criar_produto(produto)
        self.mensagem()

    def ler_produto(self):
        produtos = self.estoque.ler_todos_produtos()
        if produtos:
            for produto in produtos:
                print(f"Nome: {produto.get('nome', 'N/A')}")
                print(f"Código de barras: {produto.get('codigoBarras', 'N/A')}")
                print(f"Preço: {produto.get('preco', 'N/A')}")
                print(f"Quantidade: {produto.get('quantidade', 'N/A')}")
                print("-" * 40)
        else:
            print("Nenhum produto cadastrado.")
        self.mensagem()


    def atualizar_produto(self):
        id = int(input("Entre com o id: "))
        preco = float(input("Entre com o novo preço: "))
        quantidade = int(input("Entre com a nova quantidade: "))
        self.estoque.atualizar_produto(id, preco, quantidade)
        self.mensagem()

    def apagar_produto(self):
        id = int(input("Entre com o id: "))
        self.estoque.apagar_produto(id)
        self.mensagem()
    
    def mensagem(self):
        print("-"*75)
        print("Bem-vindo ao controle de estoque!")
        print("O que deseja acessar:")
        print("     1- Adicionar produto;")
        print("     2- Listar produtos;")
        print("     3- Atualizar produto;")
        print("     4- Apagar produto;")
        print("Digite 'sair' para encerrar.") 
        
    def run(self):
        self.mensagem()
        super().run()
        # Indicar que voltou ao menu
        print("-"*75)
        print("Bem-vindo ao Sistema de Gerenciamento do Supermercado!")
        print("O que deseja acessar:")
        print("     1- Controle de estoque;")
        print("     2- Gerência de funcionários e setores;")
        print("Digite 'sair' para encerrar.")  

# CLI para gerência de funcionários e setores
class FuncionariosCLI(SimpleCLI):
    def __init__(self, funcionarios: FuncionariosCRUD):
        super().__init__()
        self.funcionarios = funcionarios
        self.add_command("1", self.criar_funcionario)
        self.add_command("2", self.ler_funcionarios)
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
        funcionario = Funcionario(nome, dataNascimento, cpf, id, telefone, email)
        print(self.funcionarios.criar_funcionario(funcionario))
        self.mensagem()

    def ler_funcionarios(self):
        funcionarios = self.funcionarios.ler_todos_funcionarios()
        if funcionarios:
            for funcionario in funcionarios:
                print(f"Nome: {funcionario['nome']}")
                print(f"Data de nascimento: {funcionario['dataNascimento']}")
                print(f"CPF: {funcionario['cpf']}")
                print(f"Telefone: {funcionario['telefone']}")
                print(f"Email: {funcionario['email']}")
                print("-" * 40)
        else:
            print("Não há funcionários cadastrados.")
        self.mensagem()

    def atualizar_funcionario(self):
        id = int(input("Entre com o id: "))
        telefone = input("Entre com o novo telefone: ")
        email = input("Entre com o novo email: ")
        self.funcionarios.atualizar_funcionario(id, telefone, email)
        self.mensagem()

    def apagar_funcionario(self):
        id = int(input("Entre com o id: "))
        self.funcionarios.apagar_funcionario(id)

    def criar_setor(self):
        id = int(input("Entre com o id: "))
        nome = float(input("Entre com o nome do setor: "))
        setor = Setor(nome, id)
        print(self.funcionarios.criar_setor(setor))
        self.mensagem()

    def ler_setor(self):
        id = int(input("Entre com o id: "))
        setor = self.funcionarios.ler_setor(id)
        if setor:
            print(f"Nome: {setor['nome']}")
        self.mensagem()

    def atualizar_setor(self):
        id = int(input("Entre com o id: "))
        nome = input("Entre com o nome: ")
        self.funcionarios.atualizar_setor(id, nome)
        self.mensagem()

    def apagar_setor(self):
        id = int(input("Enter the id: "))
        self.funcionarios.apagar_setor(id)
        self.mensagem()

    def funcionario_setor(self):
        funcionario = input("Entre com o nome do funcionário: ")
        setor = input("Entre com o nome do setor: ")
        print(self.funcionarios.funcionario_setor(funcionario, setor))
        self.mensagem()
    
    def funcionario_gerente(self):
        gerente = input("Entre com o nome do gerente: ")
        funcionario = input("Entre com o nome do funcionário: ")
        print(self.funcionarios.funcionario_gerente(funcionario, gerente))
        self.mensagem()
    
    def mensagem(self):
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

    def run(self):
        self.mensagem()
        super().run()
        # Indicar que voltou ao menu
        print("-"*75)
        print("Bem-vindo ao Sistema de Gerenciamento do Supermercado!")
        print("O que deseja acessar:")
        print("     1- Controle de estoque;")
        print("     2- Gerência de funcionários e setores;")
        print("Digite 'sair' para encerrar.") 