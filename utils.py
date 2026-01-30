import sqlite3
import os

def clear_terminal():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS/Posix
        _ = os.system('clear')



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

def pegar_infos(userid):
    userid = int(userid)
    cursor.execute(
        "SELECT nome FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    nome = row[0] if row else None

    cursor.execute(
        "SELECT dinheiro FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    dinheiro = row[0] if row else None

    cursor.execute(
        "SELECT emprestimo FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    emprestimo = row[0] if row else None

    cursor.execute(
        "SELECT pixkey FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    pixkey = row[0] if row else None

    return nome, dinheiro, emprestimo, pixkey


def mudar_pix(pix, userid):
    cursor.execute(
    "UPDATE users SET pixkey = ? WHERE id = ?",
    (pix, userid)
    )
    conn.commit()

def pagar_emprestimo(user_id, valor):
    cursor.execute(
        "UPDATE users \
         SET dinheiro = dinheiro - ? \
         WHERE id = ? AND dinheiro >= ?",
        (valor, user_id, valor)
    )
    conn.commit()

    cursor.execute(
        "UPDATE users \
         SET emprestimo = 0 \
         WHERE id = ?",
        (user_id,)
    )
    conn.commit()

def solicitar_emprestimo(userid, valor):
    cursor.execute(
        "UPDATE users \
         SET dinheiro = dinheiro + ? \
         WHERE id = ? ",
        (valor, userid)
    )
    conn.commit()
    cursor.execute(
        "UPDATE users \
         SET emprestimo = emprestimo + ? \
         WHERE id = ? ",
        (valor, userid)
    )
    conn.commit()