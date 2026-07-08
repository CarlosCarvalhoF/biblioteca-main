
class Livro:
    def __init__(self, codigo: str, titulo: str, autor: str, categoria: str):
        if not codigo or str(codigo).strip() == "":
            raise ValueError("Código não pode ser vazio.")
        
        if not str(codigo).strip().isdigit():
            raise ValueError("Código deve conter apenas números.")
            
        if not titulo or str(titulo).strip() == "":
            raise ValueError("Título não pode ser vazio.")
            
        if not autor or str(autor).strip() == "":
            raise ValueError("Autor não pode ser vazio.")
            
        if not categoria or str(categoria).strip() == "":
            raise ValueError("Categoria não pode ser vazio.")
        
        self.codigo = str(codigo).strip()
        self.titulo = str(titulo).strip()
        self.autor = str(autor).strip()
        self.categoria = str(categoria).strip()
        self.disponivel = True

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"[{self.codigo}] {self.titulo} - Autor: {self.autor} | Cat: {self.categoria} | Status: {status}")