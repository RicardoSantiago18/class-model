from university import Universidade
from department import Departamento
from teacher import Professor
from subject import Disciplina

def main():
    # Criando uma universidade
    universidade = Universidade("Universidade Exemplo", "Rua da Educação, 123", "1990")

    # Criando departamentos
    depto_ciencia = Departamento("Ciências Exatas", "CEX")
    depto_humanas = Departamento("Ciências Humanas", "CHU")

    # Adicionando departamentos à universidade
    universidade.adicionarDepartamento(depto_ciencia)
    universidade.adicionarDepartamento(depto_humanas)

    # Criando professores
    prof_maria = Professor("Maria Silva", "12345", "Matemática")
    prof_joao = Professor("João Souza", "67890", "História")

    # Adicionando professores aos departamentos
    depto_ciencia.adicionarProfessor(prof_maria)
    depto_humanas.adicionarProfessor(prof_joao)

    # Criando disciplinas
    disciplina_matematica = Disciplina("Matemática Avançada", "MAT101", 60, 4)
    disciplina_historia = Disciplina("História do Brasil", "HIS202", 45, 3)

    # Atribuindo disciplinas aos professores
    prof_maria.adicionarDisciplina(disciplina_matematica)
    prof_joao.adicionarDisciplina(disciplina_historia)

    # Definindo o professor responsável pela disciplina
    disciplina_matematica.definirProfessor(prof_maria)
    disciplina_historia.definirProfessor(prof_joao)

    # Exibindo informações
    print(universidade.obterInformacoes())
    universidade.listarDepartamentos()

    print(depto_ciencia.obterInformacoes())
    depto_ciencia.listarProfessores()

    print(prof_maria.obterInformacoes())
    prof_maria.listarDisciplinas()

    print(disciplina_matematica.obterDetalhes())

if __name__ == "__main__":
    main()
