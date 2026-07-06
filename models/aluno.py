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
