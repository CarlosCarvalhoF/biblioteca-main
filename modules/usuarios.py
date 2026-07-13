from aluno import Aluno
from dados import alunos

def validar_nome(nome):
    nome = nome.strip()

    if nome == "":
        return False

    if len(nome) < 3:
        return False

    for caractere in nome:
        if not (caractere.isalpha() or caractere.isspace()):
            return False

    return True

def validar_telefone(telefone):
    telefone = telefone.strip()

    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace("-", "")
    telefone = telefone.replace(" ", "")

    if not telefone.isdigit():
        return None

    if len(telefone) != 10 and len(telefone) != 11:
        return None

    return telefone

def validar_turma(turma):
    turma = turma.strip()

    if turma == "":
        return False

    if len(turma) > 20:
        return False

    return True

def validar_nome_mae(nome):
    return validar_nome(nome)

def validar_cpf(cpf, lista):
    if len(cpf) != 11 or not cpf.isdigit():
        return None # Retorna None (Já tornando inválido na validação do cadastro)
    for aluno in lista: # Percorre a lista de alunos
        if cpf == aluno.cpf: # Verifica se o CPF já consta
            print('CPF ja existe')
            return None # Se existir, retorna None (Tornando inválida a validação do cadastro) 
    return cpf

def validar_matricula(matricula, lista):
    if matricula == '':
        return None # Retorna None (Já tornando inválido na validação do cadastro)
    for aluno in lista: # Percorre a lista de alunos
        if matricula == aluno.matricula: # Verifica se a matrícula já consta
            print('Matricula ja existe')
            return None # Se existir, retorna None (Tornando inválida a validação do cadastro) 
    return matricula

def cadastrar_aluno(): # Função para cadastro de novos alunos
    print("--- CADASTRO DE ALUNO ---")
    
    matricula = (input('Digite a matrícula: ')).strip() # Solicitação de informação
    while validar_matricula(matricula, alunos) is None: # Validação da informação; enquanto inválida, continuará solicitando
        matricula = (input('Digite nova matrícula: ')).strip()
    
    nome = input('Digite o nome do aluno: ').strip() # Solicita o nome
    while not validar_nome(nome): # Se o nome for inválido, solicitará novamente
        nome = input('O nome digitado é inválido. Digite um nome válido:').strip()

    turma = input('Turma: ').strip()
    while not validar_turma(turma): # Validação da informação; enquanto inválida, continuará solicitando     
        turma = input('turma inválida, tente novamente:').strip()

    cpf = input('Digite o CPF: ') # Solicitação de informação
    while validar_cpf(cpf, alunos) is None: # Validação da informação; enquanto inválida, continuará solicitando
        cpf = (input('Digite o cpf com 11 digitos: ')).strip() 
    
    nome_mae = input('Digite o nome da mãe: ')
    while not validar_nome_mae(nome_mae):
        nome_mae = input('O nome da mãe digitado é inválido. Digite um nome válido: ').strip()

    telefone = input('Contato: ')
    while validar_telefone(telefone) is None: # Validação da informação; enquanto inválida, continuará solicitando
        telefone = (input('O telefone digitado é inválido. Digite um telefone válido: ')).strip()
    telefone = validar_telefone(telefone) # Atualiza a variável para salvar o número já limpo

    aluno = Aluno(matricula, nome, turma, cpf, nome_mae, telefone, emprestimos_ativos = 0, total_emprestimos = 0) # Cria o objeto Aluno com as informações solicitadas 
    
    alunos.append(aluno) # Salva o objeto Aluno na lista de alunos
    print('Aluno cadastrado com SUCESSO!\n')

def listar_alunos(lista): # Função para listar alunos
    if len(lista) == 0: # Se a lista estiver vazia
        print('Nenhum aluno encontrado!') # Exibe mensagem de retorno 
    else: 
        print("--- Lista de Alunos ---")
        for aluno in lista: # Percorre a lista de alunos e exibe suas informações
            print(f"""Matrícula: {aluno.matricula} | Nome: {aluno.nome} | Turma: {aluno.turma} | Telefone: {aluno.telefone} | Nome da mãe: {aluno.nome_mae} | CPF: {aluno.cpf}
""", 100*'-') 
        
def buscar_aluno(matricula, lista): # Busca um aluno com base na matrícula
    for aluno in lista: # Percorre a lista de alunos
        if aluno.matricula == matricula: # Verifica se a matrícula digitada existe
            return aluno # Retorna o objeto Aluno
    return None # Se não encontrar o aluno, retorna None (vazio)
