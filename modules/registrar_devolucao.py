def contabilizar_devolucoes(historico_devolucoes: list) -> dict:

    total = len(historico_devolucoes)

    if total == 0:
        return {"total": 0, "mensagem": "Nenhuma devolução registrada ainda."}

    no_prazo = 0
    com_atraso = 0

    for devolucao in historico_devolucoes:
        if devolucao.get("atraso_dias", 0) > 0:
            com_atraso += 1
        else:
            no_prazo += 1

    return {
        "total": total,
        "no_prazo": no_prazo,
        "com_atraso": com_atraso,
        "mensagem": f"{total} devolução(ões) registrada(s).",
    }


def tela_registro_devolucoes(repositorio: RepositorioLivros):
    print("\n── REGISTRO DE DEVOLUÇÕES ──")
    livros = repositorio.listar()
    historico = []

    for livro in livros:
        for emp in livro.emprestimos:
            if emp.status == StatusEmprestimo.ENCERRADO:
                atraso = (emp.data_devolucao - emp.data_emprestimo).days
                historico.append({
                    "codigo": livro.codigo,
                    "titulo": livro.titulo,
                    "usuario": emp.usuario,
                    "atraso_dias": max(0, atraso - 7)
                })

    resultado = contabilizar_devolucoes(historico)
    print(f"\n  {resultado['mensagem']}")
    if resultado["total"] > 0:
        print(f"  No prazo  : {resultado['no_prazo']}")
        print(f"  Com atraso: {resultado['com_atraso']}")