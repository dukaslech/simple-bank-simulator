import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


def criar_conta(nome, email, senha):

    cursor.execute(
        "INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)",
        (nome, email, senha)
    )
    conn.commit()


def procurar_infos(nome=None, email=None):
    query = "SELECT * FROM users WHERE 1=1"
    params = []

    if nome is not None:
        query += " AND nome = ?"
        params.append(nome)

    if email is not None:
        query += " AND email = ?"
        params.append(email)

    cursor.execute(query, params)
    return cursor.fetchone()

def logar(email, senha):
    cursor.execute(
        "SELECT id FROM users WHERE email = ? AND senha = ?",
        (email, senha)
    )
    row = cursor.fetchone()
    return row[0] if row else None
