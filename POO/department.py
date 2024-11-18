class Departamento:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.professores = []

    def adicionarProfessor(self, professor):
        if professor not in self.professores and len(self.professores) < 5:
            self.professores.append(professor)


    def removerProfessor(self, professor):
        if professor in self.professores:
            self.professores.remove(professor)
            print(f"Professor {professor.nome} foi removido do Departamento {self.nome}.")

    def listarProfessores(self):
        if self.professores:
            for professor in self.professores:
                print(f"Professor: {professor.nome}")
        else:
            print("Nenhum professor cadastrado neste departamento.")
