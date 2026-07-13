from modules.gerenciadorLivros import (
    cadastrar_livro,
    listar_livros,
    buscar_livro
)

from models.usuarios import (
    cadastrar_aluno,
    listar_alunos,
    buscar_aluno
)

from models.modules.emprestimos import realizar_emprestimo
from modules.devolucoes import devolver_livro
from modules.historico import listar_historico
from modules.relatorios import menu_relatorios

def menu():

    while True:

        print("\n========== BIBLIOTECA ==========")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Buscar Livro")
        print("4 - Cadastrar Aluno")
        print("5 - Listar Alunos")
        print("6 - Buscar Aluno")
        print("7 - Realizar Empréstimo")
        print("8 - Devolver Livro")
        print("9 - Histórico")
        print("10 - Relatórios")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()

        elif opcao == "2":
            listar_livros()

        elif opcao == "3":
            buscar_livro()

        elif opcao == "4":
            cadastrar_aluno()

        elif opcao == "5":
            listar_alunos()

        elif opcao == "6":
            buscar_aluno()

        elif opcao == "7":
            realizar_emprestimo()

        elif opcao == "8":
            devolver_livro()

        elif opcao == "9":
            listar_historico()

        elif opcao == "10":
            menu_relatorios()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")
