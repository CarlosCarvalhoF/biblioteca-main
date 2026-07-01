from collections import Counter
from modelos import Livro, Usuario, Emprestimo
 
 
class RelatorioBiblioteca:
    def __init__(self, livros: list[Livro], usuarios: list[Usuario], emprestimos: list[Emprestimo]):
        self.livros = livros
        self.usuarios = usuarios
        self.emprestimos = emprestimos
 
    # Livros disponíveis
    def livros_disponiveis(self):
        return [livro for livro in self.livros if livro.disponivel]
 
    # Livros emprestados
    def livros_emprestados(self):
        return [livro for livro in self.livros if not livro.disponivel]
 
    # Ranking de usuários
    def ranking_usuarios(self, top_n: int = None):
        contagem = Counter(e.usuario_id for e in self.emprestimos)
        ranking = []
        for usuario in self.usuarios:
            qtd = contagem.get(usuario.id, 0)
            ranking.append((usuario, qtd))
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
        for posicao, (usuario, qtd) in enumerate(self.ranking_usuarios(), start=1):
            linhas.append(f"  {posicao}º - {usuario.nome}: {qtd} empréstimo(s)")
 
        linhas.append("=" * 45)
        return "\n".join(linhas)