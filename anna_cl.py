list_students = []
list_registration = []
list_birth_date = []

while True:
    choice = input("""
MENU
=====================
1 - Adicionar aluno
2 - Listar todos alunos
Escolha: """)

    if choice == "1":
        name = input("Nome: ")
        list_students.append(name)
        registration = input("Matrícula: ")
        list_registration.append(registration)
        birth_date = input("Nascimento: ")
        list_birth_date.append(birth_date)
        print(f'\n1{name} - {registration} - {birth_date}')

    if choice == "2":
        for student in range (len(list_students)):
            print(f'{student+1}. {list_students[student]} - {list_registration[student]} - {list_birth_date[student]}')