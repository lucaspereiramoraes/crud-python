from crud import (
cadastrar_pessoas,
listar_pessoas,
pesquisar_pessoas,
editar_pessoa,
remover_pessoas
)

from database import criar_tabela

from utils import (
ler_inteiro
)


def menu() -> int:

    """
    Exibe o menu principal do sistema.

    Returns:
        int: Opção escolhida pelo usuário.
    """

    criar_tabela()

    print('-' * 23)
    print('OPÇÕES'.center(23))
    print('-' * 23)
    print('1 - Novo cadastro')
    print('2 - Listar cadastros')
    print('3 - Pesquisar cadastro')
    print('4 - Editar cadastro')
    print('5 - Remover cadastro')
    print('6 - Sair')
    print('-' * 23)

    return ler_inteiro('Digite a opção correspondente:')

while True:
    opcao = menu()
    if opcao == 1:
        cadastrar_pessoas()
    elif opcao == 2:
        listar_pessoas()
    elif opcao == 3:
        pesquisar_pessoas()
    elif opcao == 4:
        editar_pessoa()
    elif opcao == 5:
        remover_pessoas()
    elif opcao == 6:
        print('Opção 6 selecionada')
        print('Saindo...')
        break
    else:
        print('Opção inválida, tente novamente!')