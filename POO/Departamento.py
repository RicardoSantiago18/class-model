from professor import Professor

class Departamento:
    def __init__(self, nome, codigo, chefe=None):
        self.nome = nome
        self.codigo = codigo
        self.chefe = chefe
        self.listaProfessores = []

    def adicionarProfessor(self, professor):
        if len(self.listaProfessores) < 5:
            self.listaProfessores.append(professor)
            professor.definirDepartamento(self)
        else:
            print("O departamento já possui o número máximo de professores (5).")

    def removerProfessor(self, professor):
        if professor in self.listaProfessores:
            self.listaProfessores.remove(professor)
            professor.removerDepartamento()

    def listarProfessores(self):
        for professor in self.listaProfessores:
            print(f"Professor: {professor.nome}")

    def obterInformacoes(self):
        return f"Departamento: {self.nome}, Código: {self.codigo}, Chefe: {self.chefe.nome if self.chefe else 'N/A'}"
