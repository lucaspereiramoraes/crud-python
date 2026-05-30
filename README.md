# CRUD de Usuários em Python

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de Python através da construção de um sistema CRUD (Create, Read, Update e Delete) para gerenciamento de usuários.

Os dados são armazenados em um arquivo JSON, permitindo a persistência das informações entre diferentes execuções do programa.

Durante o desenvolvimento foram aplicados conceitos importantes como modularização, manipulação de arquivos, tratamento de exceções, validações, documentação com docstrings e utilização de type hints.

---

## Funcionalidades

* Cadastrar usuários
* Listar usuários cadastrados
* Pesquisar usuários por nome
* Visualizar dados de um usuário
* Editar cadastros existentes
* Remover usuários
* Armazenamento em arquivo JSON
* Validação de nome, celular e e-mail
* Tratamento de erros e exceções

---

## Tecnologias Utilizadas

* Python 3
* JSON
* Biblioteca padrão do Python

---

## Estrutura do Projeto

```text
crud-usuarios-python/
│
├── main.py
├── crud.py
├── utils.py
├── usuarios.json
└── README.md
```

### Arquivos

**main.py**

* Ponto de entrada da aplicação.
* Responsável pelo menu principal e controle do fluxo do sistema.

**crud.py**

* Contém as operações principais do CRUD.
* Cadastro, listagem, pesquisa, edição e remoção de usuários.

**utils.py**

* Contém funções auxiliares de validação, manipulação de arquivos, busca, seleção e exibição de dados.

---

## Conceitos Praticados

* Funções
* Modularização
* Estruturas condicionais
* Estruturas de repetição
* Manipulação de arquivos
* Manipulação de JSON
* Tratamento de exceções
* Docstrings
* Type Hints
* Organização de código
* Boas práticas de programação

---

## Como Executar

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
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

Este projeto foi desenvolvido como parte da minha jornada de aprendizado em desenvolvimento de software, com foco na prática dos fundamentos da linguagem Python e na construção de aplicações organizadas e bem documentadas.

---

## Melhorias Futuras

* Implementar testes automatizados
* Utilizar banco de dados em vez de arquivo JSON
* Criar interface gráfica
* Desenvolver versão web da aplicação
* Melhorar sistema de busca e filtros

---

## Autor

Lucas Moraes
