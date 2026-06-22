from utils import (
    ler_inteiro, validar_email, validar_celular, validar_nome, escolher_cadastro, dados_usuario,
    interrupcao_sistema
)


from database import (
    inserir_usuario, listar_usuarios, buscar_pessoas_db, atualizar_usuario, deletar_usuario
)

def cadastrar_pessoas() -> None:

    """
    Realiza o cadastro de um novo usuario.

    Solicita nome, celular e e-mail do usuario,
    valida os dados informados e salva o cadastro
    no banco de dados SQLite.
    """

    nome = validar_nome('Nome:')

    celular = validar_celular('Celular: ')

    email = validar_email('E-mail:')

    inserir_usuario(nome, celular, email)

    print('Cadastro realizado com sucesso!')



def listar_pessoas() -> None:

    """
    Lista os usuários cadastrados no sistema.

    Recupera os dados do banco de dados e,
    se existirem registros, exibe os usuários.
    """

    dados = listar_usuarios()

    pessoa_escolhida = escolher_cadastro(dados)

    if pessoa_escolhida:
        dados_usuario(pessoa_escolhida)


def pesquisar_pessoas() -> None:

    """
    Pesquisa usuários no banco de dados pelo nome e exibe o cadastro selecionado.

    Solicita um termo de busca, consulta o banco SQLite e, se houver resultados,
    permite selecionar um usuário para visualização.
    """
    pesquisa = interrupcao_sistema('Digite o nome desejado (ENTER para listar todos): ').strip().lower()

    pessoas = buscar_pessoas_db(pesquisa)

    if not pessoas:
        print('Nenhum cadastro localizado!')
        return

    pessoa_escolhida = escolher_cadastro(pessoas)

    if pessoa_escolhida:
        dados_usuario(pessoa_escolhida)


def editar_pessoa() -> None:

    """
    Permite editar um cadastro existente no banco de dados.

    O usuário pode pesquisar uma pessoa pelo nome,
    selecionar um registro e alterar nome, celular ou e-mail.

    As alterações são persistidas diretamente no banco de dados
    através da função atualizar_usuario().
    """

    pesquisa = interrupcao_sistema('Digite o nome desejado (ENTER para listar todos): ').strip().lower()

    pessoas = buscar_pessoas_db(pesquisa)

    if not pessoas:
        print('Nenhum cadastro localizado!')
        return

    pessoa_escolhida = escolher_cadastro(pessoas)

    if not pessoa_escolhida:
        return

    nome = pessoa_escolhida['nome']
    email = pessoa_escolhida['email']
    celular = pessoa_escolhida['celular']

    while True:
        print('-' * 23)
        print('OPÇÕES'.center(23))
        print('-' * 23)
        print('0 - Voltar')
        print('1 - Nome')
        print('2 - Celular')
        print('3 - E-mail')
        print('4 - Finalizar')
        print('-' * 23)

        while True:
            ...
            opcao_edicao = ler_inteiro('Qual dado deseja alterar?')

            if opcao_edicao == 0:
                return

            elif opcao_edicao == 1:
                nome = validar_nome('Novo nome: ')

            elif opcao_edicao == 2:
                celular = validar_celular('Novo celular: ')

            elif opcao_edicao == 3:
                email = validar_email('Novo E-mail: ')

            elif opcao_edicao == 4:
                atualizar_usuario(pessoa_escolhida['id'], nome, email, celular)
                print('Alteração realizada com sucesso!')
                return


def remover_pessoas() -> None:

    """
    Remove um usuário cadastrado no banco de dados.

    Permite pesquisar usuários pelo nome ou listar todos,
    selecionar um cadastro e confirmar a exclusão.

    Após confirmação, o usuário é removido do banco de dados.

    Returns:
        None
    """

    pesquisa = interrupcao_sistema('Digite o nome desejado (ENTER para listar todos): ').strip().lower()

    pessoas = buscar_pessoas_db(pesquisa)

    pessoa_escolhida = escolher_cadastro(pessoas)

    if not pessoa_escolhida:
        return

    while True:
        print('-' * 23)
        print('OPÇÕES'.center(23))
        print('-' * 23)
        print('1 - Sim')
        print('2 - Não')
        print('-' * 23)

        confirmacao = ler_inteiro('Confirmar exclusão: ')

        if confirmacao == 1:

            deletar_usuario(pessoa_escolhida['id'])

            print('Cadastro excluído com sucesso!')
            break

        elif confirmacao == 2:
            print('Exclusão não realizada!')
            break

        else:
            print('Opção inválida, tente novamente')