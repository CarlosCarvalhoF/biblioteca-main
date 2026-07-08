from modules.gerenciadorLivros import listar_livros
from usuarios import listar_alunos
from modules.emprestimos import realizar_emprestimo
from modules.aluno import Aluno
 
class Relatorio:
    def __init__(self, listar_livros, listar_alunos, realizar_emprestimo):
        self.listar_livros = listar_livros
        self.listar_alunos = listar_alunos
        self.realizar_emprestimo = realizar_emprestimo
 
    def livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.listar_livros() if livro.disponivel]
        if not livros_disponiveis:
            print("Nenhum livro disponível no momento.")
            return
        return livros_disponiveis
 
    def livros_emprestados(self):
        livros_emprestados = [livro for livro in self.listar_livros() if not livro.disponivel]
        if not livros_emprestados:
            print("Nenhum livro emprestado no momento.")
            return
        return livros_emprestados
 
       
    def ranking_alunos(self):
        listar_alunos = sorted(
            self.listar_alunos(),
            key=lambda aluno: aluno.total_emprestimos,
            reverse=True
        )
        if not listar_alunos:
            print("Nenhum aluno cadastrado no momento.")
            return
        return listar_alunos
   
def menu_relatorios():
    relatorio = Relatorio(listar_livros, listar_alunos, None)
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Livros Disponíveis")
        print("2. Livros Emprestados")
        print("3. Ranking de Alunos")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            livros_disponiveis = relatorio.livros_disponiveis()
            if livros_disponiveis:
                print("\n--- Livros Disponíveis ---")
                for livro in livros_disponiveis:
                    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
        elif opcao == "2":
            livros_emprestados = relatorio.livros_emprestados()
            if livros_emprestados:
                print("\n--- Livros Emprestados ---")
                for livro in livros_emprestados:
                    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")
        elif opcao == "3":
            ranking_alunos = relatorio.ranking_alunos()
            if ranking_alunos:
                print("\n--- Ranking de Alunos ---")
                for aluno in ranking_alunos:
                    print(f"Nome: {aluno.nome}, Total de Empréstimos: {aluno.total_emprestimos}")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
 
