class Departamento:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.professores = []

    def adicionarProfessor(self, professor):
        if len(self.professores) < 5:
            if professor not in self.professores:
                self.professores.append(professor)
                print(f"Professor {professor.nome} associado ao departamento {self.nome}.")
            else:
                print("O professor já está associado a este departamento.")
        else:
            print("Número máximo de professores atingido!")

    def listarProfessores(self):
        for professor in self.professores:
            print(f"Professor: {professor.nome}, Área: {professor.area}")

    def removerProfessor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            print(f"Professor {professor.nome} removido do departamento {self.nome}.")
        else:
            print("O professor não está associado a este departamento.")
