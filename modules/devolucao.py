from datetime import datetime
from dados import livros 

def devolver_livro():
    print("\n========== DEVOLVER LIVRO ==========")
    codigo_digitado = input("Digite o código do livro que está devolvendo: ").strip()

    livro_encontrado = None
    for livro in livros:
        if livro.codigo == codigo_digitado:
            livro_encontrado = livro
            break

    if livro_encontrado == None:
        print("Erro: Livro não encontrado no sistema.")
        return

    if livro_encontrado.disponivel == True:
        print("Aviso: Este livro não está emprestado.")
        return

    try:
        data_hoje = datetime.now()
        dias_com_livro = (data_hoje - livro_encontrado.data_emprestimo).days

        if dias_com_livro > 7:
            atraso = dias_com_livro - 7
            print(f"Atenção: Livro devolvido com {atraso} dia(s) de atraso!")
        else:
            print("Devolução realizada dentro do prazo de 7 dias.")
            
    except Exception:
        print("Aviso: Data de empréstimo não registrada.")

    livro_encontrado.disponivel = True
    print(f"Sucesso! O livro '{livro_encontrado.titulo}' voltou para a prateleira.")