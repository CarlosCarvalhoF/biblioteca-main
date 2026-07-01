import biblioteca

def realizar_emprestimo():
    print("--- REALIZAR EMPRÉSTIMO---")

    busca_1 = input('Digite a matricula do aluno: ').strip()

    aluno_encontrado = None

    for aluno in biblioteca.lista_alunos:
        if aluno.matricula == busca_1:
            aluno_encontrado = aluno
            print('Aluno encontrado!')
            break
    if aluno_encontrado is None:
        print('Aluno não encontrado!')
        return

    busca_2 = input('Digite o codigo do livro: ')

    livro_encontrado = None

    for livro in biblioteca.lista_livros:
        if livro['codigo'] == busca_2:
            livro_encontrado = livro
            print('livro encontrado!')
            break
    if livro_encontrado is None:
        print('Livro não encontrado!')
        return
    
    status = livro['status']
    if status == 'disponível':
        
        livro['status'] = 'emprestado'
        print('Empréstimo realizado com sucesso!')
    else:
        print('Livro indisponível para empréstimo!')