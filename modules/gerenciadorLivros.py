from dados import livros
from models.Livro import Livro

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