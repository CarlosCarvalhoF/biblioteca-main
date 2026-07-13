#Lestat & Barbara
from datetime import datetime # importa a biblioteca para definir datas
from dados import livros, alunos, emprestimos # importa as listas do modulo dados

def realizar_emprestimo():
    print("--- REALIZAR EMPRÉSTIMO---")

    # Localiza o aluno pela matricula
    busca_1 = input('Digite a matricula do aluno: ').strip() 

    aluno_encontrado = None

    for aluno in alunos:
        if aluno.matricula == busca_1:
            aluno_encontrado = aluno
            print('Aluno encontrado!')
            break

    if aluno_encontrado is None: #Interrompe o processo se o nome do aluno for invalido
        print('Aluno não encontrado!')
        return

    # Localiza o livro pelo codigo
    busca_2 = input('Digite o codigo do livro: ').strip()

    livro_encontrado = None

    for livro in livros:
        if livro.codigo == busca_2:
            livro_encontrado = livro
            print('livro encontrado!')
            break
        
    if livro_encontrado is None: # interrompe o processo se o livro for invalido
        print('Livro não encontrado!')
        return
    
    # verifica a disponibilidade e registra o emprestimo na lista
    if livro_encontrado.disponivel:
        livro_encontrado.disponivel = False
        livro_encontrado.data_emprestimo = datetime.now()

        aluno_encontrado.emprestimos_ativos += 1
        aluno_encontrado.total_emprestimos += 1

        registro = {
            "Aluno": aluno_encontrado,
            "Livro": livro_encontrado,
            "Data": livro_encontrado.data_emprestimo # Nota: importante adicionarem self data_emprestimo na classe livro
        }
        emprestimos.append(registro)
        
        print('Empréstimo realizado com sucesso!')
    else:
        print('Livro indisponível para empréstimo!')
