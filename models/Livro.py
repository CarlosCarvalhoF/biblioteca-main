class Livro:
    def __init__(self, codigo: str, titulo: str, autor: str, categoria: str):
        self.codigo = str(codigo).strip()
        self.titulo = str(titulo).strip()
        self.autor = str(autor).strip()
        self.categoria = str(categoria).strip()
        self.disponivel = True

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"[{self.codigo}] {self.titulo} - Autor: {self.autor} | Cat: {self.categoria} | Status: {status}")