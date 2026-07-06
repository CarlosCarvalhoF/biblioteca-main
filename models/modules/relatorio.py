from collections import Counter

from models.modules.gerenciadorLivros import Livro, listar_livros
from models.usuarios import listar_alunos, Aluno
from models.modules.gerenciadorLivros import listar_livros

 
class RelatorioBiblioteca:
    def __init__(self, livros: list[listar_livros], alunos: list[listar_alunos], emprestimos: list[listar_livros]):
        self.livros = livros
        self.usuarios = alunos
        self.emprestimos = emprestimos
 
    # Livros disponíveis
    def livros_disponiveis(self):
        return [Livro for Livro in self.livros if Livro.disponivel]
 
    # Livros emprestados
    def livros_emprestados(self):
        return [Livro for Livro in self.livros if not Livro.disponivel]
 
    # Ranking de usuários
    def ranking_alunos(self, top_n: int = None):
        contagem = Counter(e.listar_alunos_id for e in self.emprestimos)
        ranking = []
        for listar_alunos in self.usuarios:
            qtd = contagem.get(listar_alunos.id, 0)
            ranking.append((listar_alunos, qtd))
        ranking.sort(key=lambda par: par[1], reverse=True)
        return ranking[:top_n] if top_n else ranking
 
    # saída formatada
    def gerar_relatorio_completo(self):
        linhas = []
        linhas.append("=" * 45)
        linhas.append("RELATÓRIO DA BIBLIOTECA")
        linhas.append("=" * 45)
 
        linhas.append(f"\n LIVROS DISPONÍVEIS ({len(self.livros_disponiveis())})")
        for livro in self.livros_disponiveis():
            linhas.append(f"  - {livro.titulo} ({livro.autor})")
 
        linhas.append(f"\n LIVROS EMPRESTADOS ({len(self.livros_emprestados())})")
        for livro in self.livros_emprestados():
            linhas.append(f"  - {livro.titulo} ({livro.autor})")
 
        linhas.append("\n RANKING DE USUÁRIOS")
        for posicao, (listar_alunos, qtd) in enumerate(self.ranking_alunos(), start=1):
            linhas.append(f"  {posicao}º - {listar_alunos.nome}: {qtd} empréstimo(s)")
 
        linhas.append("=" * 45)
        return "\n".join(linhas)
