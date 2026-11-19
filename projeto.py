#projeto academico

cursos = []
disciplinas = []
professores = []
alunos = []
notas = []


# cadastro de cursos
def cadastrar_aluno():
    
    matricula = int(input("digite a matrícula: "))
    nome = input("digite o nome do aluno: ")
    curso = input("digite o curso: ")
    
    aluno = {
        "matricula": matricula,
        "nome": nome,
        "curso": curso
    }
    
    alunos.append(aluno)
    
    print("aluno cadastrado com sucesso!")
    
def cadastrar_curso():
    
    codigo = int(input("cadastre o codigo do curso: "))
    curso = input("cadastre o curso: ")
    
    curso = {
        "curso": curso,
        "codigo": codigo
    }
    
    cursos.append(curso)
    
    print("curso cadastrado com sucesso!")
    
def cadastrar_disciplina():
    
    disciplina = input("cadastrar disciplina: ")
    codigo = int(input("cdastre o codigo da disciplina: "))
    
    disciplina = {
        "disciplina": disciplina,
        "codigo": codigo
    }
    
    disciplinas.append(disciplina)
    
    print("disciplina cadastrada com sucesso")
    
def cadastrar_professor():
    
    matricula = int(input("cadastrar matricula: "))
    disciplina = input("cadastrar disciplina: ")
    nome = input("cadastre seu nome: ")
    curso = input("cadastre seu curso: ")
    
    professor = {
        "matricula": matricula,
        "disciplina": disciplina,
        "nome": nome,
        "curso": curso
    }
    
    professores.append(professor)
    
    print("professor cadastrado(a) com suceso!")
    
def cadastrar_notas():

    matricula = int(input("digite sua maticula: "))    
#   aluno = input("qual aluno ira receber a nota: ")
    disciplina = input("de qual disciplina é essa nota:  ")
    nota = float(input("cadastre a nota: "))

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            aluno_matriculado = True
            break
    if aluno_matriculado:
        registro = {
            "matricula": matricula,
            "disciplina": disciplina,
            "nota": nota
        }

        notas.append(registro)
        print("nota cadastrada")
    else:
        print("aluno não encontrado")


def concluir_curso():

    matricula = int(input("digite sua matricula: "))
    lista_notas = []

    for registro in notas:
        if registro["matricula"] == matricula:
            lista_notas.append(registro["nota"])

    if len(lista_notas) == 0:
        print("nenhuma nota encontrada")
        return

    media = sum(lista_notas) / len(lista_notas)
    print("notas:", lista_notas)
    print("media:", round(media, 2))

    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado! ")
#menu de interação
while True:

    print("\n===== SISTEMA ACADÊMICO =====")
    print("1 - Cadastrar curso")
    print("2 - Cadastrar disciplina")
    print("3 - Cadastrar professor")
    print("4 - Cadastrar aluno")
    print("5 - Cadastrar notas")
    print("6 - Consultar aprovação")
    print("7 - Relatórios")
    print("8 - Emitir certificado")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_curso()

    elif opcao == "2":
        cadastrar_disciplina()

    elif opcao == "3":
        cadastrar_professor()

    elif opcao == "4":
        cadastrar_aluno()

    elif opcao == "5":
        cadastrar_notas()

    elif opcao == "6":
        consultar_aprovacao()

    elif opcao == "7":
        gerar_relatorios()

    elif opcao == "8":
        emitir_certificado()

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")