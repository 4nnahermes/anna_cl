lista_alunos = []
lista_matricula = []
lista_data = []

while True:
    escolha = input("""
MENU
=====================
1 - Adicionar aluno
2 - Listar todos alunos
Escolha: """)

    if escolha == "1":
        nome = input("Nome: ")
        lista_alunos.append(nome)
        matricula = input("Matrícula: ")
        lista_matricula.append(matricula)
        data = input("Nascimento: ")
        lista_data.append(data)
        print(f'\n1{nome} - {matricula} - {data}')

    if escolha == "2":
        for cont in range (len(lista_alunos)):
            print(f'{cont+1}. {lista_alunos[cont]} - {lista_matricula[cont]} - {lista_data[cont]}')
