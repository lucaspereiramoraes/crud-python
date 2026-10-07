# CRUD de Usuários em Python

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Python através da construção de um sistema CRUD (Create, Read, Update e Delete) para gerenciamento de usuários.

Os dados são armazenados em um banco de dados SQLite, permitindo a persistência das informações entre diferentes execuções do programa.

Durante o desenvolvimento foram aplicados conceitos importantes como modularização, manipulação de arquivos, tratamento de exceções, validações, documentação com docstrings e utilização de type hints.

---

## Funcionalidades

* Cadastrar usuários
* Listar usuários cadastrados
* Pesquisar usuários por nome
* Visualizar dados de um usuário
* Editar cadastros existentes
* Remover usuários
* Armazenamento em banco de dados SQLite
* Validação de nome, celular e e-mail
* Tratamento de erros e exceções

---

## Tecnologias Utilizadas

* Python 3
* SQLite3 (banco de dados)
* Biblioteca padrão do Python
* Biblioteca sqlite3

---

## Estrutura do Projeto

```text
crud-usuarios-python/
│
├── main.py
├── crud.py
├── utils.py
├── database.py
├── crud.db
└── README.md
```

### Arquivos

**main.py**

* Ponto de entrada da aplicação.
* Responsável pelo menu principal e controle do fluxo do sistema.

**crud.py**

* Contém as operações principais do CRUD.
* Cadastro, listagem, pesquisa, edição e remoção de usuários.

**database.py**

* Responsável pela conexão com o banco de dados SQLite.
* Contém a criação de tabelas e funções base de acesso ao banco.

**utils.py**

* Contém funções auxiliares de validação, manipulação de arquivos, busca, seleção e exibição de dados.

---

## Conceitos Praticados

* Funções
* Modularização
* Estruturas condicionais
* Estruturas de repetição
* Manipulação de banco de dados (SQLite)
* Tratamento de exceções
* Docstrings
* Type Hints
* Organização de código
* Boas práticas de programação

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/lucaspereiramoraes/crud-python
```

2. Entre na pasta do projeto:

```bash
cd crud-usuarios-python
```

3. Execute o programa:

```bash
python main.py
```

---

## Objetivo

O sistema evoluiu ao longo do desenvolvimento, migrando de armazenamento em arquivos JSON para um banco de dados SQLite, com o objetivo de praticar conceitos mais próximos de aplicações reais.

---

## Melhorias Futuras

* Implementar testes automatizados
* Criar interface gráfica
* Desenvolver versão web da aplicação
* Melhorar sistema de busca e filtros
* Aplicar arquitetura orientada a objetos (OOP)
* Criar API REST com Flask ou FastAPI

---

## Autor

Lucas Moraes
