from dados import livros

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

def cadastrar_livro():
    print("\n========== CADASTRAR LIVRO ==========")
    codigo = input("Digite o código do livro (apenas números): ")
    
    for livro in livros:
        if livro.codigo == codigo.strip():
            print("Erro: Já existe um livro cadastrado com este código.")
            return

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    categoria = input("Digite a categoria do livro: ")

    try:
        novo_livro = Livro(codigo, titulo, autor, categoria)
        livros.append(novo_livro)
        print("Livro cadastrado com sucesso!")
        
    except ValueError as e:
        print(f"Erro no cadastro: {e}")

def listar_livros():
    print("\n========== LISTAR LIVROS ==========")
    if not livros:
        print("Nenhum livro cadastrado no sistema.")
        return

    for livro in livros:
        livro.exibir_detalhes()

def buscar_livro():
    print("\n========== BUSCAR LIVRO ==========")
    if not livros:
        print("Nenhum livro cadastrado para busca.")
        return

    termo = input("Digite o título ou o código do livro: ").strip().lower()
    encontrado = False

    for livro in livros:
        if termo == livro.codigo or termo in livro.titulo.lower():
            livro.exibir_detalhes()
            encontrado = True

    if not encontrado:
        print("Nenhum livro foi encontrado com o termo digitado.")