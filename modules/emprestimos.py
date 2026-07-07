#Lestat & Barbara

import usuarios, gerenciadorLivros

def realizar_emprestimo():
    print("--- REALIZAR EMPRÉSTIMO---")

    busca_1 = input('Digite a matricula do aluno: ').strip()

    aluno_encontrado = None

    for aluno in usuarios.lista_alunos:
        if aluno.matricula == busca_1:
            aluno_encontrado = aluno
            print('Aluno encontrado!')
            break

    if aluno_encontrado is None:
        print('Aluno não encontrado!')
        return

    busca_2 = input('Digite o codigo do livro: ').strip()

    livro_encontrado = None

    for livro in gerenciadorLivros.livros:
        if livro.codigo == busca_2:
            livro_encontrado = livro
            print('livro encontrado!')
            break
        
    if livro_encontrado is None:
        print('Livro não encontrado!')
        return
    
    if livro_encontrado.disponivel:
        livro_encontrado.disponivel = False

        livro_encontrado.emprestimos_ativos += 1
        livro_encontrado.total_emprestimos += 1

        
        print('Empréstimo realizado com sucesso!')
    else:
        print('Livro indisponível para empréstimo!')
