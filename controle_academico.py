#import.funcao

cursos = []
disciplinas = []
professores = []
alunos = []
notas = []




while True:
    print("\n===== SISTEMA ACADEMICO=====")
    print("1 - cadastrar curso")
    print("2 - cadastrar disciplina")
    print("3 - cadastrar professor")
    print("4 - cadastrar aluno")
    print("5 - cadastrar notas")
    print("6 - consultar aprovação")
    print("7 - relatorios")
    print("8 - emitir certificado")
    print("9 - ver cadastros")
    print("0 - sair")
    
    opcao = input("escolha uma opção: ")
    
    if opcao == "1":
        print("cadastro de curso")
        
    elif opcao == "2":
        print("cadastro de disciplina")
    
    elif opcao == "3":
        print("cadastro de professor")
        
    elif opcao == "4":
        print("cadastro de aluno")
        
    elif opcao == "5":
        print("cadastrar notas")
        
    elif opcao == "6":
        print("consultar aprovação")
        
    elif opcao == "7":
        print("relatorios")
        
    elif opcao == "8":
        print("emisão de certificado")
        
    elif opcao == "9":
        print("ver cadastros")
        if opcao == "9":
            print(cursos, disciplinas, professores, alunos, notas)
        else:
            print("nada consta")
#acho que esse else ficou inutil pq ele nunca vai aparecer, mas eu não sabia se dava pra deixar o if sem o else ;)
    elif opcao == "0":
        print("sair")
        break
    
    else:
        print("opção invalida")
        
    
    