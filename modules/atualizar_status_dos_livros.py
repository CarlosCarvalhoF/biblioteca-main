#Pedro Henrique

def atualizar_status_livro(codigo_livro, livros):
    for livro in livros:
        if livro ["codigo"] == codigo_livro:
            livro["disponivel"] = False
            print("Status do livro atualizado.")
            return
 
    print("Livro não encontrado.")
 
 
livros = [
    {"codigo": "L001", "titulo": "Dom Casmurro", "disponivel": True},
    {"codigo": "L002", "titulo": "O Pequeno Príncipe", "disponivel": True}
]
 
atualizar_status_livro("L001", livros)
print(livros)
 
[
    {"codigo": "L001", "titulo": "Dom Casmurro", "disponivel": False},
    {"codigo": "L002", "titulo": "O Pequeno Príncipe", "disponivel": True}
]
 
for livro in livros:
    if livro["disponivel"]:
        print(livro["titulo"])
