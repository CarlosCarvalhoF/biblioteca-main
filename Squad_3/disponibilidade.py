#Henrique

# =============================================================================
# MÓDULO: VALIDAÇÃO DE DISPONIBILIDADE
# Responsável: Controle de empréstimos e devoluções de livros
# =============================================================================

# Importa as listas globais e classes do módulo principal
# (ajuste o nome do arquivo conforme o projeto do grupo)
# from biblioteca import lista_livros, lista_alunos


# =============================================================================
# LISTA GLOBAL DE EMPRÉSTIMOS
# =============================================================================

# Cada empréstimo é um dicionário com:
# { "codigo_livro": str, "matricula_aluno": str, "data_emprestimo": str }
lista_emprestimos = []


# =============================================================================
# FUNÇÕES AUXILIARES (uso interno)
# =============================================================================

def _buscar_livro_por_codigo(codigo: str, lista_livros: list):
    """
    Busca e retorna um livro da lista pelo código.
    Retorna None se não encontrado.
    """
    codigo = codigo.strip()
    for livro in lista_livros:
        # Suporte tanto a dicionários (cadastrar_livro) quanto a objetos Livro
        codigo_livro = livro["codigo"] if isinstance(livro, dict) else livro.codigo
        if codigo_livro == codigo:
            return livro
    return None


def _buscar_aluno_por_matricula(matricula: str, lista_alunos: list):
    """
    Busca e retorna um aluno da lista pela matrícula.
    Retorna None se não encontrado.
    """
    matricula = matricula.strip()
    for aluno in lista_alunos:
        # Objetos Usuario usam property .matricula
        if aluno.matricula == matricula:
            return aluno
    return None


def _get_status_livro(livro) -> str:
    """
    Retorna o status do livro independente de ser dict ou objeto Livro.
    """
    if isinstance(livro, dict):
        return livro.get("status", "disponível")
    return "disponível" if livro.disponivel else "emprestado"


def _set_status_livro(livro, status: str):
    """
    Atualiza o status do livro independente de ser dict ou objeto Livro.
    """
    if isinstance(livro, dict):
        livro["status"] = status
    else:
        livro.disponivel = (status == "disponível")


# =============================================================================
# FUNÇÃO: VERIFICAR DISPONIBILIDADE
# =============================================================================

def verificar_disponibilidade(lista_livros: list):
    """
    Permite consultar se um livro específico está disponível ou emprestado.

    Regras de Negócio:
    - O código informado deve corresponder a um livro cadastrado.
    - Exibe claramente o status atual do livro.

    Critérios de Aceitação:
    - Retorna e exibe "Disponível" ou "Emprestado".
    - Informa os dados do empréstimo ativo, se houver.
    """
    print("\n--- VERIFICAR DISPONIBILIDADE ---")

    # Validação: código obrigatório
    while True:
        codigo = input("Digite o código do livro: ").strip()
        if codigo:
            break
        print("❌ Erro: O código é obrigatório.")

    # Regra de Negócio: livro deve estar cadastrado
    livro = _buscar_livro_por_codigo(codigo, lista_livros)
    if not livro:
        print(f"❌ Erro: Nenhum livro encontrado com o código '{codigo}'.")
        return None

    # Exibe os dados do livro
    titulo = livro["titulo"] if isinstance(livro, dict) else livro.titulo
    autor  = livro["autor"]  if isinstance(livro, dict) else livro.autor
    status = _get_status_livro(livro)

    print(f"\n📖 Livro: {titulo} — {autor}")
    print(f"   Status: {'✅ Disponível' if status == 'disponível' else '🔴 Emprestado'}")

    # Se emprestado, mostra para quem
    if status != "disponível":
        for emp in lista_emprestimos:
            if emp["codigo_livro"] == codigo:
                print(f"   Emprestado para a matrícula: {emp['matricula_aluno']}")
                print(f"   Data do empréstimo: {emp['data_emprestimo']}")
                break

    return status


# =============================================================================
# FUNÇÃO: REGISTRAR EMPRÉSTIMO
# =============================================================================

def registrar_emprestimo(lista_livros: list, lista_alunos: list):
    """
    Registra o empréstimo de um livro a um aluno.

    Regras de Negócio:
    - O livro deve estar cadastrado.
    - O aluno deve estar cadastrado.
    - O livro deve estar disponível (não pode estar emprestado).
    - Um aluno não pode ter dois empréstimos do mesmo livro ao mesmo tempo.

    Critérios de Aceitação:
    - Status do livro alterado para 'emprestado'.
    - Empréstimo salvo na lista_emprestimos com data.
    """
    print("\n--- REGISTRAR EMPRÉSTIMO ---")

    # Validação: código do livro
    while True:
        codigo = input("Código do livro a emprestar: ").strip()
        if codigo:
            break
        print("❌ Erro: O código é obrigatório.")

    # Regra de Negócio: livro deve existir
    livro = _buscar_livro_por_codigo(codigo, lista_livros)
    if not livro:
        print(f"❌ Erro: Nenhum livro encontrado com o código '{codigo}'.")
        return None

    # Regra de Negócio: livro deve estar disponível
    if _get_status_livro(livro) != "disponível":
        titulo = livro["titulo"] if isinstance(livro, dict) else livro.titulo
        print(f"❌ Erro: O livro '{titulo}' já está emprestado e não pode ser emprestado novamente.")
        return None

    # Validação: matrícula do aluno
    while True:
        matricula = input("Matrícula do aluno: ").strip()
        if matricula:
            break
        print("❌ Erro: A matrícula é obrigatória.")

    # Regra de Negócio: aluno deve existir
    aluno = _buscar_aluno_por_matricula(matricula, lista_alunos)
    if not aluno:
        print(f"❌ Erro: Nenhum aluno encontrado com a matrícula '{matricula}'.")
        return None

    # Regra de Negócio: aluno não pode ter o mesmo livro duas vezes
    for emp in lista_emprestimos:
        if emp["codigo_livro"] == codigo and emp["matricula_aluno"] == matricula:
            print("❌ Erro: Este aluno já possui este livro emprestado.")
            return None

    # Coleta a data do empréstimo
    while True:
        data = input("Data do empréstimo (DD/MM/AAAA): ").strip()
        if data:
            break
        print("❌ Erro: A data é obrigatória.")

    # Atualiza o status do livro para 'emprestado'
    _set_status_livro(livro, "emprestado")

    # Critério de Aceitação: empréstimo salvo
    novo_emprestimo = {
        "codigo_livro": codigo,
        "matricula_aluno": matricula,
        "data_emprestimo": data
    }
    lista_emprestimos.append(novo_emprestimo)

    titulo = livro["titulo"] if isinstance(livro, dict) else livro.titulo
    print(f"\n✅ Empréstimo registrado! '{titulo}' emprestado para {aluno.nome} em {data}.")
    return novo_emprestimo


# =============================================================================
# FUNÇÃO: REGISTRAR DEVOLUÇÃO
# =============================================================================

def registrar_devolucao(lista_livros: list):
    """
    Registra a devolução de um livro emprestado.

    Regras de Negócio:
    - O livro deve estar cadastrado.
    - O livro deve estar com status 'emprestado' para ser devolvido.

    Critérios de Aceitação:
    - Status do livro alterado para 'disponível'.
    - Registro de empréstimo removido da lista_emprestimos.
    """
    print("\n--- REGISTRAR DEVOLUÇÃO ---")

    # Validação: código obrigatório
    while True:
        codigo = input("Código do livro a devolver: ").strip()
        if codigo:
            break
        print("❌ Erro: O código é obrigatório.")

    # Regra de Negócio: livro deve existir
    livro = _buscar_livro_por_codigo(codigo, lista_livros)
    if not livro:
        print(f"❌ Erro: Nenhum livro encontrado com o código '{codigo}'.")
        return False

    # Regra de Negócio: só pode devolver o que está emprestado
    if _get_status_livro(livro) == "disponível":
        titulo = livro["titulo"] if isinstance(livro, dict) else livro.titulo
        print(f"❌ Erro: O livro '{titulo}' já está disponível e não precisa ser devolvido.")
        return False

    # Remove o registro de empréstimo ativo
    emprestimo_removido = None
    for emp in lista_emprestimos:
        if emp["codigo_livro"] == codigo:
            emprestimo_removido = emp
            break

    if emprestimo_removido:
        lista_emprestimos.remove(emprestimo_removido)

    # Atualiza o status do livro para 'disponível'
    _set_status_livro(livro, "disponível")

    titulo = livro["titulo"] if isinstance(livro, dict) else livro.titulo
    print(f"\n✅ Devolução registrada! O livro '{titulo}' está disponível novamente.")
    return True


# =============================================================================
# FUNÇÃO: LISTAR TODOS OS EMPRÉSTIMOS ATIVOS
# =============================================================================

def listar_emprestimos_ativos(lista_livros: list, lista_alunos: list):
    """
    Exibe todos os empréstimos atualmente ativos.

    Critério de Aceitação:
    - Lista todos os livros emprestados com o nome do aluno e a data.
    - Informa quando não há empréstimos ativos.
    """
    print("\n--- EMPRÉSTIMOS ATIVOS ---")

    if not lista_emprestimos:
        print("ℹ️  Nenhum empréstimo ativo no momento.")
        return

    for i, emp in enumerate(lista_emprestimos, start=1):
        livro = _buscar_livro_por_codigo(emp["codigo_livro"], lista_livros)
        aluno = _buscar_aluno_por_matricula(emp["matricula_aluno"], lista_alunos)

        titulo  = livro["titulo"] if livro and isinstance(livro, dict) else (livro.titulo if livro else "Livro não encontrado")
        nome    = aluno.nome if aluno else "Aluno não encontrado"

        print(f"  {i}. 📖 {titulo} → 👤 {nome} (matrícula: {emp['matricula_aluno']}) | Data: {emp['data_emprestimo']}")

    print(f"\n  Total de empréstimos ativos: {len(lista_emprestimos)}")
