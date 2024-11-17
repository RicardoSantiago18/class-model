from POO.department import Departamento
from POO.subject import Disciplina
from POO.teacher import Professor
from POO.university import Universidade


def main():
    # Criando uma universidade
    usp = Universidade("USP")

    # Criando departamentos
    dep_computacao = Departamento("Computação")
    dep_matematica = Departamento("Matemática")

    # Adicionando departamentos à universidade
    usp.adicionar_departamento(dep_computacao)
    usp.adicionar_departamento(dep_matematica)

    # Criando professores
    prof1 = Professor("João Silva", "P001")
    prof2 = Professor("Maria Santos", "P002")
    prof3 = Professor("Pedro Costa", "P003")

    # Adicionando professores aos departamentos
    dep_computacao.adicionar_professor(prof1)
    dep_computacao.adicionar_professor(prof2)
    dep_matematica.adicionar_professor(prof3)

    # Criando disciplinas
    algoritmos = Disciplina("Algoritmos", "CC001")
    programacao = Disciplina("Programação", "CC002")
    calculo = Disciplina("Cálculo I", "MAT001")

    # Associando professores às disciplinas
    algoritmos.adicionar_professor(prof1)
    programacao.adicionar_professor(prof1)
    programacao.adicionar_professor(prof2)
    calculo.adicionar_professor(prof3)

    print("=== Estado Inicial ===")
    print(usp)
    for dep in usp.departamentos:
        print(f"\n{dep}")
        for prof in dep.professores:
            print(f"  {prof}")
            for disc in prof.disciplinas:
                print(f"    {disc}")

    print("\n=== Desativando um Departamento ===")
    dep_computacao.desativar()
    print(dep_computacao)
    print(prof1)  # Professor do departamento desativado
    print(algoritmos)  # Disciplina que era do professor

    print("\n=== Desativando a Universidade ===")
    usp.desativar()
    print(usp)
    print(dep_matematica)  # Departamento que restava
    print(prof3)  # Professor do departamento de matemática
    print(calculo)  # Disciplina que era do professor

if __name__ == "__main__":
    main()