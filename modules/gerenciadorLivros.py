from dados import livros
from models.Livro import Livro
 
def cadastrar_livro():
    print("\n========== CADASTRAR LIVRO ==========")
    codigo = input("Digite o código do livro (apenas números [positivos]): ").strip()
    while not codigo:
        print("Erro: O código do livro não pode ser vazio.")
        codigo = input("Digite o código do livro (apenas números [positivos]): ").strip()
 
    while not codigo.isnumeric():
        print("Erro: O código do livro deve conter apenas números (positivos).")
        codigo = input("Digite o código do livro (apenas números [positivos]): ").strip()
 
    for livro in livros:
        if livro.codigo == codigo:
            print("Erro: Já existe um livro cadastrado com este código.")
            return
        
    
 
    print("")
    titulo = input("Digite o título do livro: ").strip()
    while not titulo:
        print("Erro: O título do livro não pode ser vazio.")
        titulo = input("Digite o título do livro: ").strip()
 
    while titulo.isnumeric():
        print("Erro: O título do livro não pode conter apenas números.")
        titulo = input("Digite o título do livro: ").strip()
 
 
    print("")
    autor = input("Digite o autor do livro: ").strip()
    while not autor:
        print("Erro: O autor do livro não pode ser vazio.")
        autor = input("Digite o autor do livro: ").strip()
 
    while autor.isnumeric():
        print("Erro: O autor do livro não pode conter apenas números.")
        autor = input("Digite o autor do livro: ").strip()

    for livro in livros:
        if livro.titulo.lower() == titulo.lower() and livro.autor.lower() == autor.lower():
            print(f"Erro: O livro '{titulo}' do autor '{autor}' já está cadastrado no codigo {livro.codigo}.")
            return
        

    print("")
    categoria = input("Digite a categoria do livro: ").strip()
    while not categoria:
        print("Erro: A categoria do livro não pode ser vazio.")
        categoria = input("Digite a categoria do livro: ").strip()
   
    while categoria.isnumeric():
        print("Erro: A categoria do livro não pode conter apenas números.")
        categoria = input("Digite a categoria do livro: ").strip()
 
 
    novo_livro = Livro(codigo, titulo, autor, categoria)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")
 
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
 