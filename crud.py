from utils import (
    carregar_dados,
    salvar_dados,
    ler_inteiro, validar_email, validar_celular, validar_nome, escolher_cadastro, dados_usuario, buscar_pessoas
)


def cadastrar_pessoas(nome_arquivo: str) -> None:

    """
    Realiza o cadastro de um novo usuário.

    Solicita nome, celular e e-mail do usuário,
    valida os dados informados e salva o cadastro
    no arquivo JSON.

    Args:
        nome_arquivo (str): Nome do arquivo JSON
        utilizado para armazenar os dados.
    """

    nome = validar_nome('Nome:')

    celular = validar_celular('Celular: ')

    email = validar_email('E-mail:')

    pessoa = {"Nome": nome, "Celular": celular, "E-mail": email}

    dados = carregar_dados(nome_arquivo)

    dados.append(pessoa)

    salvar_dados(nome_arquivo, dados)

    print('Cadastro realizado com sucesso!')



def listar_pessoas(nome_arquivo: str) -> None:

    """
    Exibe a lista de usuários cadastrados.

    Carrega os dados do arquivo JSON e mostra
    os usuários cadastrados em ordem alfabética.

    Permite selecionar um cadastro para visualizar
    os dados do usuário.

    Args:
        nome_arquivo (str): Nome do arquivo JSON
        utilizado para armazenar os dados.
    """

    dados = carregar_dados(nome_arquivo)

    pessoa_escolhida = escolher_cadastro(dados)

    if pessoa_escolhida:
        dados_usuario(pessoa_escolhida)


def pesquisar_pessoas(nome_arquivo: str) -> None:

    """
    Pesquisa usuários cadastrados pelo nome.

    Carrega os dados do arquivo JSON e permite
    buscar usuários pelo nome completo ou por
    letras iniciais. Caso existam resultados,
    exibe os dados do cadastro selecionado.

    Args:
        nome_arquivo (str): Nome do arquivo JSON
        utilizado para armazenar os dados.
    """

    dados = carregar_dados(nome_arquivo)

    pessoas = buscar_pessoas(dados)

    pessoa_escolhida = escolher_cadastro(pessoas)

    if pessoa_escolhida:
        dados_usuario(pessoa_escolhida)


def editar_pessoa(nome_arquivo: str) -> None:

    """
    Altera os dados de um cadastro existente.

    Carrega os usuários armazenados no arquivo JSON,
    permite pesquisar um cadastro e exibe opções
    para editar nome, celular ou e-mail.

    Após a alteração, os dados atualizados são
    salvos no arquivo JSON.

    Args:
        nome_arquivo (str): Nome do arquivo JSON
        utilizado para armazenar os dados.
    """

    dados = carregar_dados(nome_arquivo)

    pessoas = buscar_pessoas(dados)

    pessoa_escolhida = escolher_cadastro(pessoas)

    if not pessoa_escolhida:
        return

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

        opcao_edicao = ler_inteiro('Qual dado deseja alterar?')

        if opcao_edicao == 0:
            return

        elif opcao_edicao == 1:
            pessoa_escolhida['Nome'] = validar_nome('Novo nome: ')

        elif opcao_edicao == 2:
            pessoa_escolhida['Celular'] = validar_celular('Novo celular: ')

        elif opcao_edicao == 3:
            pessoa_escolhida['E-mail'] = validar_email('Novo E-mail:')

        elif opcao_edicao == 4:
            salvar_dados(nome_arquivo, dados)

            print('Alteração realizada com sucesso!')
            break

        else:
            print('Opção inválida, tente novamente!')


def remover_pessoas(nome_arquivo: str) -> None:

    """
    Remove um usuário da lista de cadastros.

    Carrega os dados do arquivo JSON, permite
    pesquisar usuários cadastrados e selecionar
    um cadastro para exclusão.

    Após a seleção, exibe uma confirmação para
    remover ou cancelar a exclusão do cadastro.

    Args:
        nome_arquivo (str): Nome do arquivo JSON
        utilizado para armazenar os dados.
    """

    dados = carregar_dados(nome_arquivo)

    pessoas = buscar_pessoas(dados)

    pessoa_escolhida = escolher_cadastro(pessoas)

    if pessoa_escolhida is None:
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

            dados.remove(pessoa_escolhida)

            salvar_dados(nome_arquivo, dados)

            print('Cadastro excluído com sucesso!')
            break

        elif confirmacao == 2:
            print('Exclusão não realizada!')
            break

        else:
            print('Opção inválida, tente novamente')