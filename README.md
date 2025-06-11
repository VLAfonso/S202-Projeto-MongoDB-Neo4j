# Projeto de S202 - Sistema de Gerenciamento de Supermercado
Repositório dedicado ao projeto final da disciplina S202 (Banco de Dados II) com o tema Sistema de Gerenciamento de Supermercado.  
O objetivo do projeto foi desenvolver um sistema para gerenciar os produtos, funcionários e setores de um supermercado.

# :memo: Informações do Projeto

## :package: Entidades
### Funcionário e Setor
- `funcionario.py` - cria o objeto funcionário para armazenar seu id, nome, data de nascimento, CPF, telefone e e-mail.
- `setor.py` - cria o objeto setor para armazer seu id e nome.
- `funcionarios_CRUD.py` - cria o CRUD do funcionário e do setor, conectando com o banco de dados Neo4j, possibilitando criar, ler, atualizar e deletar funcionários e setores. Além disso, cria relacionamento de trabalho entre um funcionário e um setor e de gerência entre dois funcionários.
### Produto
- `produtos.py` - cria o objeto produto para armazenar seu id, nome, código de barras, preço e quantidade.
- `estoque_CRUD.py` - cria o CRUD do produto, conectando com o banco de dados MongoDB, possibilitando criar, ler, atualizar e deletar produtos.

## :card_file_box: Bancos de Dados
Para a conexão com os bancos de dados foi utilizado o Docker. Os bancos utilizados foram:
### MongoDB:
Banco de dados orientado a documentos, utilizado para o controle de estoque e armazenamento das informações dos produtos.  
![image](https://github.com/user-attachments/assets/906f8853-05a7-4562-aca9-541b414acfda)  
- `database_mongodb.py` - realiza a conexão do projeto com o MongoDB, por meio da biblioteca pymongo.
- `dataset_mongodb.py` - possui os dados iniciais a serem adicionados ao banco de dados.
- `schema.json` - armazena as regras de validação dos dados a serem armazenados.

### Neo4j:
Banco de dados oriendado a grafos, utilizado para a gestão dos funcionários, incluindo seus dados, as relações entre si e a associação com os diferentes setores do supermercado.  
![image](https://github.com/user-attachments/assets/e23bf4e7-ed59-4106-b2b7-f5f5ad3f5f95)  
- `database_neo4j.py` - realiza a conexão do projeto com o Neo4j, por meio da biblioteca neo4j.
- `dataset_neo4j.py` - possui os dados iniciais a serem adicionados ao banco de dados.


## :computer: Interface
A interface do sistema é feita por meio de uma Interface de Linha de Comando (CLI), que possibilita o usuário gerenciar o supermercado, controlando o estoque e gerenciando os funcionários e setores por meio de um menu de opções.
- `cli.py` - controla a CLI, subdividindo em:
    - InicialCLI - menu inicial, que controla qual submenu será acessado;
    ![image](https://github.com/user-attachments/assets/ff547ebd-f1ab-495b-a4d6-4117c5859f93)
    - EstoqueCLI - submenu, que apresenta os controles do estoque;
    ![image](https://github.com/user-attachments/assets/ad3566a7-2c7f-4cb2-be72-499346ea08aa)
    - FuncionariosCLI - submenu, que apresenta os controles de funcionários e setores.
    ![image](https://github.com/user-attachments/assets/7acc83ef-16cc-4995-974c-b45ac7729bfe)
    

## :gear: Controle
Toda a inicialização de instâncias, conexão com os bancos de dados e inicialização do menu de controle é feito pelo arquivo main.
- `main.py` - cria as instâncias para a conexão com os bancos de dados e do CRUD de estoque, funcionários e setores. Além de inserir os dados iniciais e instanciar e iniciar a CLI.

# :hammer_and_wrench: Tecnologias e Ferramentas Utilizadas
- Linguagem de Programação: Python
- Bancos de Dados: MongoDB e Neo4j
- Ferramentas: Docker e VisualStudioCode

# :busts_in_silhouette: Desenvolvedores

[Lucas Lima Gadbem](https://github.com/LucasLimaGadbem)  
[Virgínia Letícia Afonso](https://github.com/VLAfonso)
