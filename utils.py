import sqlite3
import os
import os
import secrets

TOKEN_FILE = "token.txt"

def logout_user():
    token = ler_token_txt()
    if not token:
        return

    cursor.execute("UPDATE users SET token = NULL WHERE token = ?", (token,))
    conn.commit()
    apagar_token_txt()

def gerar_token() -> str:
    return secrets.token_hex(32)

def salvar_token_txt(token: str):
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        f.write(token)

def ler_token_txt():
    try:
        with open(TOKEN_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def apagar_token_txt():
    try:
        os.remove(TOKEN_FILE)
    except FileNotFoundError:
        pass

def set_token_db(user_id: int, token: str):
    cursor.execute("UPDATE users SET token = ? WHERE id = ?", (token, user_id))
    conn.commit()

def get_user_by_token(token: str):
    cursor.execute("SELECT id FROM users WHERE token = ?", (token,))
    row = cursor.fetchone()
    return row[0] if row else None

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

def pegar_infos2(userid):
    userid = int(userid)
    cursor.execute(
        "SELECT nome FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    tnome = row[0] if row else None

    cursor.execute(
        "SELECT dinheiro FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    tdinheiro = row[0] if row else None

    cursor.execute(
        "SELECT emprestimo FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    temprestimo = row[0] if row else None

    cursor.execute(
        "SELECT pixkey FROM users WHERE id = ?",
        (userid,)
    )
    row = cursor.fetchone()
    tpixkey = row[0] if row else None

    return tnome, tdinheiro, temprestimo, tpixkey


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

def procurar_chave_dix(chave):
    query = "SELECT id FROM users WHERE 1=1 and pixkey = ?"
    
    cursor.execute("SELECT id FROM users WHERE 1=1 and pixkey = ?", (chave,))
    row = cursor.fetchone()
    sla = row[0] if row else None
    return sla

if procurar_chave_dix("admin") == 4:
    print('foi')

def transferir(userid, idtrans, valor):
    cursor.execute(
        "UPDATE users \
         SET dinheiro = dinheiro - ? \
         WHERE id = ? ",
        (valor, userid)
    )
    conn.commit()
    cursor.execute(
        "UPDATE users \
         SET dinheiro = dinheiro + ? \
         WHERE id = ? ",
        (valor, idtrans)
    )
    conn.commit()