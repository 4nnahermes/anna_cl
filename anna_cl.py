lalunos = []
lmatricula = []
ldata = []

while True:
    esc = input("""
MENU
=====================
1 - Adicionar aluno
2 - Listar todos alunos
Escolha: """)

# entrada de dados
    if esc == "1":
        nome = input("Nome: ")
        lalunos.append(nome)
        matricula = input("Matrícula: ")
        lmatricula.append(matricula)
        data = input("Nascimento: ")
        ldata.append(data)
        print(f'\n1{nome} - {matricula} - {data}')

# print da lista de alunos cadastrados
    if esc == "2":
        for cont in range (len(lalunos)):
            print(f'{cont+1}. {lalunos[cont]} - {lmatricula[cont]} - {ldata[cont]}')