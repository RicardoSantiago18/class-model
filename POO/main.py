from university import Universidade
from department import Departamento
from teacher import Professor
from subject import Disciplina


def main():
    universidade = Universidade("Universidade Estadual do Amazonas")

    # Criando departamentos
    departamento_01 = Departamento("Departamento 01", "D001")
    departamento_02 = Departamento("Departamento 02", "D002")

    # Adicionando departamentos à universidade
    universidade.adicionarDepartamento(departamento_01)
    universidade.adicionarDepartamento(departamento_02)

    # Criando professores
    professor1 = Professor("Marie Curie", "P001", "Química")
    professor2 = Professor("Sandro Curió", "P002", "Matemática Aplicada")
    professor3 = Professor("Rubens Paiva", "P003", "História")
    professor4 = Professor("Isaac Newton", "P004", "Astronomia")

    professores = [professor1, professor2, professor3, professor4]

    # Adicionando professores aos departamentos
    departamento_01.adicionarProfessor(professor1)
    departamento_02.adicionarProfessor(professor2)
    departamento_01.adicionarProfessor(professor3)
    departamento_02.adicionarProfessor(professor4)

    # Criando disciplinas
    disciplina1 = Disciplina("Química I", "MEX001")
    disciplina2 = Disciplina("Álgebra Linear", "MEX002")
    disciplina3 = Disciplina("Cálculo I", "MEX003")
    disciplina4 = Disciplina("História", "MEX004")
    disciplina5 = Disciplina("Física", "MEX005")

    # Associando disciplinas aos professores
    professor1.adicionarDisciplina(disciplina1)
    professor2.adicionarDisciplina(disciplina2)
    professor2.adicionarDisciplina(disciplina3)
    professor3.adicionarDisciplina(disciplina4)
    professor4.adicionarDisciplina(disciplina5)


    print(f"=== {universidade.nome} ===\n")

    print("Departamentos:")
    for departamento in universidade.departamentos:
        print(f"- {departamento.nome}")

    print("\nProfessores por Departamento:")
    for departamento in universidade.departamentos:
        print(f"- {departamento.nome}:")
        for professor in departamento.professores:
            print(f"  - {professor.nome} ({professor.especialidade})")

    print("\nDisciplinas Ministradas:")
    for professor in professores:
        for disciplina in professor.disciplinas:
            print(f"- {disciplina.nome}: Professor {professor.nome}")

if __name__ == "__main__":
    main()
