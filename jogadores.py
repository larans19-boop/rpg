def incluir(conn, nome, apelido):
    """
    Insere um novo jogador.
    Retorna o id gerado.
    """
    cursor = conn.execute(
        "INSERT INTO jogadores (nome, apelido) VALUES (?, ?)", 
        (nome, apelido)
    )
    conn.commit()
    return cursor.lastrowid


def buscar_por_id(conn, id):
    """
    Busca um jogador pelo id.
    Retorna uma tupla (id, nome, apelido) ou None se não existir.
    """
    cursor = conn.execute(
        "SELECT id, nome, apelido FROM jogadores WHERE id = ?", 
        (id,)
    )
    return cursor.fetchone()


def buscar_por_nome(conn, nome):
    """
    Busca jogadores que contêm a string 'nome' (busca parcial, sem diferenciar maiúsculas/minúsculas no LIKE padrão).
    Retorna uma lista de tuplas (id, nome, apelido).
    """
    cursor = conn.execute(
        "SELECT id, nome, apelido FROM jogadores WHERE nome LIKE ? ORDER BY nome", 
        ("%" + nome + "%",)
    )
    return cursor.fetchall()


def listar(conn):
    """
    Lista todos os jogadores ordenados por id.
    Retorna uma lista de tuplas (id, nome, apelido).
    """
    cursor = conn.execute("SELECT id, nome, apelido FROM jogadores ORDER BY id")
    return cursor.fetchall()
