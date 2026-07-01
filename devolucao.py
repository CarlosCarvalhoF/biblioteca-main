from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional




PRAZO_DEVOLUCAO_DIAS = 7  



class StatusLivro(Enum):
    DISPONIVEL = "disponível"
    EMPRESTADO = "emprestado"


class StatusEmprestimo(Enum):
    ATIVO = "ativo"
    ENCERRADO = "encerrado"




@dataclass
class Emprestimo:
    id: int
    codigo_livro: int
    usuario: str
    data_emprestimo: datetime
    status: StatusEmprestimo = StatusEmprestimo.ATIVO
    data_devolucao: Optional[datetime] = None
    dias_atraso: int = 0

    @property
    def prazo_devolucao(self) -> datetime:
        """Prazo de Devolução: data do empréstimo + prazo em dias (7 dias)."""
        return self.data_emprestimo + timedelta(days=PRAZO_DEVOLUCAO_DIAS)


@dataclass
class Livro:
    codigo: int
    titulo: str
    autor: str
    status: StatusLivro = StatusLivro.DISPONIVEL
    emprestimos: list[Emprestimo] = field(default_factory=list)

    def emprestimo_ativo(self) -> Optional[Emprestimo]:
        return next(
            (e for e in self.emprestimos if e.status == StatusEmprestimo.ATIVO),
            None,
        )




class LivroNaoEncontradoError(Exception):
    def __init__(self, codigo: int):
        super().__init__(f"Livro '{codigo}' não encontrado no sistema.")
        self.codigo = codigo


class EmprestimoNaoAtivoError(Exception):
    def __init__(self, codigo: int):
        super().__init__(f"Livro '{codigo}' não possui empréstimo ativo.")
        self.codigo = codigo


class DevolucaoDuplicadaError(Exception):
    def __init__(self, codigo: int):
        super().__init__(f"Livro '{codigo}' já foi devolvido anteriormente.")
        self.codigo = codigo



class RepositorioLivros:
    def __init__(self):
        self._livros: dict[int, Livro] = {}

    def adicionar(self, livro: Livro) -> None:
        self._livros[livro.codigo] = livro

    def buscar(self, codigo: int) -> Optional[Livro]:
        return self._livros.get(codigo)

    def salvar(self, livro: Livro) -> None:
        self._livros[livro.codigo] = livro



class BibliotecaService:
   

    def __init__(self, repositorio: RepositorioLivros):
        self.repositorio = repositorio

    def devolver_livro(self, codigo_livro: int) -> Emprestimo:
       
        livro = self.repositorio.buscar(codigo_livro)
        if livro is None:
            raise LivroNaoEncontradoError(codigo_livro)

        
        emprestimo = livro.emprestimo_ativo()
        if emprestimo is None:
            if livro.status == StatusLivro.DISPONIVEL and livro.emprestimos:
                raise DevolucaoDuplicadaError(codigo_livro)
            raise EmprestimoNaoAtivoError(codigo_livro)

        
        data_atual = datetime.now()
        prazo_devolucao = emprestimo.prazo_devolucao

        if data_atual > prazo_devolucao:
            dias_atraso = (data_atual - prazo_devolucao).days
        else:
            dias_atraso = 0

        
        emprestimo.data_devolucao = data_atual
        emprestimo.dias_atraso = dias_atraso
        emprestimo.status = StatusEmprestimo.ENCERRADO

        
        disponivel = True
        livro.status = StatusLivro.DISPONIVEL if disponivel else StatusLivro.EMPRESTADO
        self.repositorio.salvar(livro)

        
        print("Livro devolvido.")
        print(f"Status atualizado: {emprestimo.status.value} / {livro.status.value}")

        if dias_atraso > 0:
            print(f"Devolução com {dias_atraso} dia(s) de atraso.")
        else:
            print("Devolução dentro do prazo.")

        if disponivel:
            print("Livro agora está disponível para outro usuário.")

        return emprestimo
