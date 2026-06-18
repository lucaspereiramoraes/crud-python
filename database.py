import sqlite3


def conectar():
    return sqlite3.connect('crud.db')



def criar_tabela():
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



def inserir_usuario(nome, email, celular):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nome, email, celular)
        VALUES (?, ?, ?)
    """, (nome, email, celular))

    conn.commit()
    conn.close()



def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conn.close()
    return usuarios



def atualizar_usuarios(id, nome, email, celular):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE usuarios 
        SET nome = ?, email = ?, celular = ?
        WHERE id = ?""", (nome, email, celular, id))

    conn.commit()
    conn.close()



def deletar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM usuarios
        WHERE id = ?""", (id,))

    conn.commit()
    conn.close()