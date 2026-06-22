# ==========================
# ENTRADA E INTERAÇÃO
# ==========================


def interrupcao_sistema(mensagem: str) -> str:

    """
    Solicita uma entrada de texto ao usuário.

    Exibe uma mensagem no terminal e retorna
    o valor informado pelo usuário.

    Trata interrupções do sistema causadas por
    KeyboardInterrupt.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        str: Texto informado pelo usuário.
    """

    while True:
        try:
            opcao = input(mensagem).strip()
        except KeyboardInterrupt:
            print('\nPrograma interrompido pelo usuário')
            exit()
        else:
            return opcao


def ler_inteiro(mensagem: str) -> int:

    """
    Solicita e valida um número inteiro.

    Exibe uma mensagem ao usuário e garante
    que o valor informado seja um número inteiro válido.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        int: Número inteiro informado pelo usuário.
    """

    while True:
        try:
            opcao = int(input(mensagem))
        except ValueError:
            print('Erro... Digite o número correspondente')
        except KeyboardInterrupt:
            print('\nPrograma interrompido pelo usuário')
            exit()
        else:
            return opcao


def ler_texto(mensagem: str) -> str:

    """
    Solicita uma entrada de texto ao usuário.

    Garante que o campo informado não
    esteja vazio.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        str: Texto informado pelo usuário.
    """

    while True:
        texto = interrupcao_sistema(mensagem)

        if texto:
            return texto

        print('Campo não pode ficar vazio!')


# ==========================
# VALIDAÇÕES
# ==========================


def validar_nome(mensagem: str) -> str:

    """
    Solicita e valida o nome do usuário.

    Permite apenas caracteres alfabéticos e
    espaços no nome informado.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        str: Nome validado informado pelo usuário.
    """

    while True:
        nome = ler_texto(mensagem)

        if nome.replace(' ' , '').isalpha():
            return nome

        print('Nome inválido. Não pode conter números. Tente novamente!')


def validar_celular(mensagem: str) -> str:

    """
    Solicita e valida o número de celular.

    Permite números com ou sem caracteres
    de formatação, como parênteses, espaços
    e hífens.

    O número deve conter 11 dígitos,
    incluindo DDD e o dígito 9.

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        str: Número de celular validado.
    """

    while True:
        cel = ler_texto(mensagem)

        cel = cel.replace('(', '')
        cel = cel.replace(')', '')
        cel = cel.replace('-', '')
        cel = cel.replace(' ', '')

        if cel.isdigit() and len(cel) == 11:
            return cel

        print('Celular inválido. Deve conter DDD + 9 + número. Tente novamente!')


def validar_email(mensagem: str) -> str:

    """
    Solicita e valida um endereço de e-mail.

    O e-mail informado deve conter os
    caracteres "@" e ".".

    Args:
        mensagem (str): Mensagem exibida ao usuário.

    Returns:
        str: E-mail validado.
    """

    while True:
        email = ler_texto(mensagem)

        if '@' in email and '.' in email:
            return email

        print('E-mail inválido. Deve conter "@" e ".". Tente novamente!')


# ==========================
# BUSCA E SELEÇÃO
# ==========================


def listar_nomes(pessoas: list[dict[str, str]]) -> None:

    """
    Exibe a lista de usuários cadastrados.

    Mostra os usuários em formato enumerado
    para permitir a seleção de um cadastro.

    Args:
        pessoas (list[dict[str, str]]): Lista de usuários cadastrados.
    """

    print('CADASTROS'.center(23, "-"))

    print('0 - Voltar')

    for indice, pessoa in enumerate(pessoas):
        print(f'{indice + 1} - {pessoa["nome"]}')

    print('-' * 23)


def escolher_cadastro(pessoas: list[dict]) -> dict | None:

    """
    Permite selecionar um usuário cadastrado.

    Exibe a lista de cadastros disponíveis e
    solicita ao usuário a escolha de um cadastro.

    Returns:
        dict | None: Retorna o cadastro selecionado
        ou None caso a operação seja cancelada.
    """

    if not pessoas:
        print('Nenhum cadastro encontrado!')
        return None

    pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa['nome'].lower())

    listar_nomes(pessoas_ordenadas)

    opcao = ler_inteiro('Escolha o cadastro:')

    if opcao == 0:
        return None

    if 1 <= opcao <= len(pessoas_ordenadas):
        return pessoas_ordenadas[opcao - 1]

    print("Opção inválida, retornando ao menu principal!")
    return None


# ==========================
# EXIBIÇÃO
# ==========================


def dados_usuario(pessoa) -> None:

    """
    Exibe os dados de um usuário cadastrado.

    Mostra nome, celular e e-mail do usuário
    selecionado.

    Args:
        pessoa (dict): Dados do usuário selecionado.
    """

    print("USUÁRIO".center(30, "-"))
    print(f"Nome: {pessoa['nome']}")
    print(f"Celular: {pessoa['celular']}")
    print(f"E-mail: {pessoa['email']}")
    print('-' * 30)