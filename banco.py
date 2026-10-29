import sqlite3


def conectar():
    conn = sqlite3.connect("rpg.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def criar_tabelas(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        apelido TEXT NOT NULL
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL,
        poder INTEGER NOT NULL
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS personagens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nivel INTEGER NOT NULL,
        jogador_id INTEGER NOT NULL,
        classe_id INTEGER NOT NULL,
        FOREIGN KEY (jogador_id) REFERENCES jogadores (id),
        FOREIGN KEY (classe_id) REFERENCES classes (id)
    );
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS inventario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        personagem_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (personagem_id) REFERENCES personagens (id),
        FOREIGN KEY (item_id) REFERENCES itens (id)
    );
    """)
    conn.commit()


def carregar_dados_exemplo(conn):
    # Classes
    conn.execute("INSERT INTO classes (nome) VALUES ('Guerreiro')")
    conn.execute("INSERT INTO classes (nome) VALUES ('Mago')")
    conn.execute("INSERT INTO classes (nome) VALUES ('Arqueiro')")
    conn.execute("INSERT INTO classes (nome) VALUES ('Clérigo')")

    # Jogadores
    conn.execute("INSERT INTO jogadores (nome, apelido) VALUES ('Ana Silva', 'Aninha')")
    conn.execute("INSERT INTO jogadores (nome, apelido) VALUES ('Bruno Costa', 'Brunao')")

    # Itens
    conn.execute("INSERT INTO itens (nome, tipo, poder) VALUES ('Espada Longa', 'Arma', 15)")
    conn.execute("INSERT INTO itens (nome, tipo, poder) VALUES ('Cajado do Fogo', 'Arma', 20)")
    conn.execute("INSERT INTO itens (nome, tipo, poder) VALUES ('Poção de Vida', 'Consumível', 50)")
    conn.execute("INSERT INTO itens (nome, tipo, poder) VALUES ('Machadinha', 'Arma', 12)")

    # Personagens
    conn.execute("INSERT INTO personagens (nome, nivel, jogador_id, classe_id) VALUES ('Arthur', 5, 1, 1)")
    conn.execute("INSERT INTO personagens (nome, nivel, jogador_id, classe_id) VALUES ('Gork', 3, 2, 1)")

    # Inventário
    conn.execute("INSERT INTO inventario (personagem_id, item_id, quantidade) VALUES (1, 1, 1)")
    conn.execute("INSERT INTO inventario (personagem_id, item_id, quantidade) VALUES (2, 4, 1)")
    conn.execute("INSERT INTO inventario (personagem_id, item_id, quantidade) VALUES (2, 3, 3)")

    conn.commit()
