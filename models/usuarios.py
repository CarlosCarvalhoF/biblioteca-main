class Aluno: #Classe aluno
    def __init__(self, matricula, nome, turma, cpf, nome_mae, telefone, emprestimos_ativos, total_emprestimos): # Metodo construtos e parâmetros
        self.matricula = matricula
        self.nome = nome
        self.turma = turma
        self.cpf = cpf
        self.nome_mae = nome_mae
        self.telefone = telefone

        self.emprestimos_ativos = emprestimos_ativos
        self.total_emprestimos = total_emprestimos
    def exibir_aluno(self): # Metodo de exibição do objeto
        print(f'''
Nome: {self.nome} | CPF: {self.cpf} | Nome da mãe: {self.nome_mae}
Matrícula: {self.matricula} | Turma: {self.turma} | Telefone: {self.telefone}''')

def validar_cpf(cpf, lista):
    if len(cpf) != 11 or not cpf.isdigit():
        return None # Retorna None (Ja tornando invalido na validação do cadastro)
    for aluno in lista: # Se houver algo, percorre a lista alunos
        if cpf == aluno.cpf: # Verifica se o CPF já consta
            print('CPF ja existe')
            return None # Se existir, retorna None (Tornando inválida a validação do cadastro) 
    return cpf
def validar_matricula(matricula, lista):
    if matricula == '':
        return None # Retorna None (Ja tornando invalido na validação do cadastro)
    for aluno in lista: # Se houver algo, percorre a lista alunos
        if matricula == aluno.matricula: # Verifica se a matrícula já consta
            print('Matricula ja existe')
            return None # Se existir, retorna None (Tornando inválida a validação do cadastro) 
    return matricula

def cadastrar_aluno(): # Função para cadastro de novos alunos
    print("--- CADASTRO DE ALUNO ---")
    
    matricula = (input('Digite a matrícula: ')).strip() # Solicitação de informação
    while validar_matricula(matricula, lista_alunos) is None: # Validação da informação, enquanto inválida continuará solicitando
        matricula = (input('Digite nova matrícula: ')).strip()
    
    nome = input('Digite o nome do aluno: ').strip() # Solicita o nome
    while nome == '': # Se estiver vazio, solicitará novamente
        nome = input('O nome não pode estar vazio, digite o nome do aluno: ').strip()

    turma = input('Turma: ').strip()
    while turma =='':
        turma = input('Turma não pode estar em branco: ').strip()

    cpf = input('Digite o CPF: ') # Solicitação de informação
    while validar_cpf(cpf, lista_alunos) is None: # Validação da informação, enquanto inválida continuará solicitando
        cpf = (input('Digite o cpf com 11 digitos: ')).strip() 
    
    nome_mae = input('Digite o nome da mãe: ')
    while nome_mae == '':
         nome_mae = input('O campo não pode estar em branco. Digite o nome da mãe: ').strip()

    telefone = input('Contato: ')
    while telefone == '':
        telefone = (input('Campo não pode estar vazio. Digite o telefone para contato: ')).strip()

    aluno = Aluno(matricula, nome, turma, cpf, nome_mae, telefone, emprestimos_ativos = 0, total_emprestimos = 0) # Cria o Objeto Aluno com as informações soliciatadas 
    
    lista_alunos.append(aluno) # Salva o objeto Aluno na lista de alunos
    print('Aluno cadastrado com SUCESSO!\n')

def listar_alunos(lista): # Função para listar Alunos
    if len(lista) == 0: # Se a lista estiver vazia
        print('Nenhum aluno encontrado!') # Retorno 
    else: 
        print("--- Lista de Alunos ---")
        for aluno in lista: # Percorre a lista de alunos e Exibe suas informações
            print(f"""Matrícula: {aluno.matricula} | Nome: {aluno.nome} | Turma: {aluno.turma} | Telefone: {aluno.telefone} | Nome da mãe: {aluno.nome_mae} | CPF: {aluno.cpf}
""", 100*'-') 
        
def buscar_aluno(matricula, lista): #Busca um Aluno com base na matrícula
    for aluno in lista: # Percorre o atributo matricula na lista alunos
        if aluno.matricula == matricula: #Verifica se a matricula digitada existe
            return aluno #Retorna o objeto Aluno
    return None # Se não encontrar nada, retorna vazio


lista_alunos = []

cadastrar_aluno()
cadastrar_aluno()

listar_alunos(lista_alunos)

matricula = (input('Digite a matricula: '))
aluno = buscar_aluno(matricula, lista_alunos)
if aluno is not None:
    aluno.exibir_aluno()
else:
    print("Aluno não encontrado")
