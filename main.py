import banco
import classes
import jogadores
import itens
import personagens
import inventario


def menu_classes(conn):
    while True:
        print("\n--- MENU CLASSES ---")
        print("1 - Incluir")
        print("2 - Buscar por ID")
        print("3 - Buscar por nome")
        print("4 - Listar todas")
        print("0 - Voltar")
        op = input("Opção: ")

        if op == "1":
            nome = input("Nome da classe: ")
            id_gerado = classes.incluir(conn, nome)
            print(f"Classe criada com ID {id_gerado}!")
        elif op == "2":
            id_busca = int(input("ID: "))
            res = classes.buscar_por_id(conn, id_busca)
            print(res if res else "Não encontrada.")
        elif op == "3":
            nome = input("Nome: ")
            res = classes.buscar_por_nome(conn, nome)
            print(res if res else "Nenhuma encontrada.")
        elif op == "4":
            res = classes.listar(conn)
            for item in res:
                print(item)
        elif op == "0":
            break


def menu_jogadores(conn):
    while True:
        print("\n--- MENU JOGADORES ---")
        print("1 - Incluir")
        print("2 - Buscar por ID")
        print("3 - Buscar por nome")
        print("4 - Listar todos")
        print("0 - Voltar")
        op = input("Opção: ")

        if op == "1":
            nome = input("Nome: ")
            apelido = input("Apelido: ")
            id_gerado = jogadores.incluir(conn, nome, apelido)
            print(f"Jogador criado com ID {id_gerado}!")
        elif op == "2":
            id_busca = int(input("ID: "))
            res = jogadores.buscar_por_id(conn, id_busca)
            print(res if res else "Não encontrado.")
        elif op == "3":
            nome = input("Nome: ")
            res = jogadores.buscar_por_nome(conn, nome)
            print(res if res else "Nenhum encontrado.")
        elif op == "4":
            res = jogadores.listar(conn)
            for item in res:
                print(item)
        elif op == "0":
            break


def menu_itens(conn):
    while True:
        print("\n--- MENU ITENS ---")
        print("1 - Incluir")
        print("2 - Buscar por ID")
        print("3 - Buscar por nome")
        print("4 - Listar todos")
        print("0 - Voltar")
        op = input("Opção: ")

        if op == "1":
            nome = input("Nome do item: ")
            tipo = input("Tipo (ex: Arma, Poção): ")
            poder = int(input("Poder: "))
            id_gerado = itens.incluir(conn, nome, tipo, poder)
            print(f"Item criado com ID {id_gerado}!")
        elif op == "2":
            id_busca = int(input("ID: "))
            res = itens.buscar_por_id(conn, id_busca)
            print(res if res else "Não encontrado.")
        elif op == "3":
            nome = input("Nome: ")
            res = itens.buscar_por_nome(conn, nome)
            print(res if res else "Nenhum encontrado.")
        elif op == "4":
            res = itens.listar(conn)
            for item in res:
                print(item)
        elif op == "0":
            break


def menu_personagens(conn):
    while True:
        print("\n--- MENU PERSONAGENS ---")
        print("1 - Incluir")
        print("2 - Buscar por ID")
        print("3 - Buscar por nome")
        print("4 - Listar todos")
        print("0 - Voltar")
        op = input("Opção: ")

        if op == "1":
            nome = input("Nome do personagem: ")
            nivel = int(input("Nível: "))
            jogador_id = int(input("ID do jogador: "))
            classe_id = int(input("ID da classe: "))
            try:
                id_gerado = personagens.incluir(conn, nome, nivel, jogador_id, classe_id)
                print(f"Personagem criado com ID {id_gerado}!")
            except Exception as e:
                print("Erro ao incluir personagem:", e)
        elif op == "2":
            id_busca = int(input("ID: "))
            res = personagens.buscar_por_id(conn, id_busca)
            print(res if res else "Não encontrado.")
        elif op == "3":
            nome = input("Nome: ")
            res = personagens.buscar_por_nome(conn, nome)
            print(res if res else "Nenhum encontrado.")
        elif op == "4":
            res = personagens.listar(conn)
            for item in res:
                print(item)
        elif op == "0":
            break


def menu_inventario(conn):
    while True:
        print("\n--- MENU INVENTÁRIO ---")
        print("1 - Incluir item no inventário")
        print("2 - Buscar por ID do inventário")
        print("3 - Buscar por nome do personagem")
        print("4 - Listar todo o inventário")
        print("0 - Voltar")
        op = input("Opção: ")

        if op == "1":
            personagem_id = int(input("ID do personagem: "))
            item_id = int(input("ID do item: "))
            quantidade = int(input("Quantidade: "))
            try:
                id_gerado = inventario.incluir(conn, personagem_id, item_id, quantidade)
                print(f"Item inserido no inventário com ID {id_gerado}!")
            except Exception as e:
                print("Erro ao inserir no inventário:", e)
        elif op == "2":
            id_busca = int(input("ID do inventário: "))
            res = inventario.buscar_por_id(conn, id_busca)
            print(res if res else "Não encontrado.")
        elif op == "3":
            nome = input("Nome do personagem: ")
            res = inventario.buscar_por_nome(conn, nome)
            print(res if res else "Nenhum registo encontrado.")
        elif op == "4":
            res = inventario.listar(conn)
            for item in res:
                print(item)
        elif op == "0":
            break


def main():
    conn = banco.conectar()
    banco.criar_tabelas(conn)

    while True:
        print("\n=== SISTEMA DE RPG ===")
        print("1 - Classes")
        print("2 - Jogadores")
        print("3 - Itens")
        print("4 - Personagens")
        print("5 - Inventário")
        print("6 - Carregar dados de exemplo")
        print("0 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            menu_classes(conn)
        elif op == "2":
            menu_jogadores(conn)
        elif op == "3":
            menu_itens(conn)
        elif op == "4":
            menu_personagens(conn)
        elif op == "5":
            menu_inventario(conn)
        elif op == "6":
            banco.carregar_dados_exemplo(conn)
            print("Dados de exemplo carregados com sucesso!")
        elif op == "0":
            conn.close()
            print("Até logo!")
            break


if __name__ == "__main__":
    main()
