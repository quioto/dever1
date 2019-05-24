# Função validar login
def listarProfessores(cursor):
    cursor.execute(f'select nome from professor ')
    professor = cursor.fetchall()
    cursor.close()
    return professor


def exibirPofessor(cursor, nome):
    cursor.execute(f'select nome, datanasc, nomedamae, titulacao from faculdade.professor where nome="{nome}"')
    prof = cursor.fetchone()
    cursor.close()
    return prof


def consultarTitulacao(cursor, parametro):
    cursor.execute(f'select nome from faculdade.professor where titulacao = {parametro}')
    consulta = cursor.fetchall()
    cursor.close()

    return consulta

def consultarapenascomputacao(cursor):
    cursor.execute(f'select professor.nome FROM professor inner join disciplina on disciplina.idprofessor = professor.idprofessor where curso = "Ciencia da Computacao"')
    curso = cursor.fetchall()
    cursor.close()
    return curso