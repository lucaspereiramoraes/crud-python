import sqlite3


def conectar() -> sqlite3.Connection:

    """
    Abre e retorna uma conexão com SQLite configurada para retornar linhas como dicionários.
    """

    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn



def criar_tabela() -> None:

    """
    Cria a tabela 'usuarios' caso ela não exista.

    Returns:
        None
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            celular TEXT
        )
    """)

    conn.commit()
    conn.close()



def inserir_usuario(nome: str, email: str, celular: str) -> None:

    """
    Insere um novo usuario na tabela 'usuarios'.

    Args:
        nome (str): Nome do usuário
        email (str): Email do usuario
        celular (str): Celular do usuário

    Returns:
        None
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, email, celular)
        VALUES (?, ?, ?)
    """, (nome, email, celular))

    conn.commit()
    conn.close()



def listar_usuarios() -> list[dict[str, str]]:

    """
    Retorna todos os usuarios cadastrados.

    Returns:
        list[dict[str, str]]: Lista contendo os registros retornados pelo banco de dados.
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios



def buscar_pessoas_db(nome: str) -> list[dict]:
    """
        Busca usuários no banco pelo nome (ou retorna todos se vazio).

    Args:
        nome (str): Nome ou parte do nome para busca.

    Returns:
        list[dict]: Usuarios encontrados.
        """

    conn = conectar()
    cursor = conn.cursor()

    if nome.strip() == "":
        cursor.execute("SELECT * FROM usuarios")
    else:
        cursor.execute(
            "SELECT * FROM usuarios WHERE nome LIKE ?",
            (f"%{nome}%",)
        )

    dados = cursor.fetchall()

    conn.close()
    return [dict(row) for row in dados]



def atualizar_usuario(id_usuario: int, nome: str, email: str, celular: str) -> None:

    """
    Atualiza um usuário na tabela usuarios.

    Args:
        id_usuario (int): Identificador do usuario
        nome (str): Novo nome do usuario
        email (str): Novo email do usuario
        celular (str): Novo celular do usuario

    Returns:
        None
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE usuarios 
        SET nome = ?, email = ?, celular = ?
        WHERE id = ?""", (nome, email, celular, id_usuario))

    conn.commit()
    conn.close()



def deletar_usuario(id_usuario: int) -> None:

    """
    Apaga um usuario na tabela usuarios.

    Args:
        id_usuario (int): Identificador do usuario que será removido.

    Returns:
        None
    """

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM usuarios
        WHERE id = ?""", (id_usuario,))

    conn.commit()
    conn.close()