from teacher import Professor
from subject import Disciplina

def main():
    professor1 = Professor("Dr. João Silva", "P001", "Matemática Aplicada")
    professor2 = Professor("Dra. Maria Oliveira", "P002", "Física Quântica")
    professor3 = Professor("Dr. Rubens Paiva", "P003", "História")


    disciplina1 = Disciplina("Cálculo I", "MAT101")
    disciplina2 = Disciplina("Álgebra Linear", "MAT102")
    disciplina3 = Disciplina("Física Clássica", "FIS101")
    disciplina4 = Disciplina("História", "FIS102")
    disciplina5 = Disciplina("Geometria Analítica", "MAT103")
    disciplina6 = Disciplina("Física Moderna", "FIS103")

    professor1.adicionarDisciplina(disciplina1)
    professor1.adicionarDisciplina(disciplina2)
    professor1.adicionarDisciplina(disciplina5)

    professor2.adicionarDisciplina(disciplina3)
    professor3.adicionarDisciplina(disciplina4)
    professor2.adicionarDisciplina(disciplina6)

    print("\nDisciplinas ministradas pelo Professor João Silva:")
    professor1.listarDisciplinas()

    print("\nDisciplinas ministradas pela Professora Maria Oliveira:")
    professor2.listarDisciplinas()

    print("\nDisciplinas ministradas pela Professor Rubens Paiva:")
    professor3.listarDisciplinas()



if __name__ == "__main__":
    main()
