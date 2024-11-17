from subject import Disciplina
class Professor:
    def init(self, nome, id, areaEspecializacao):
        self.nome = nome
        self.id = id
        self.areaEspecializacao = areaEspecializacao
        self.departamento = None  # Associação (1 Professor pertence a 1 Departamento)
        self.listaDisciplinas = []  # Associação (1 Professor leciona 1..5 Disciplinas)

    def definirDepartamento(self, departamento):
        self.departamento = departamento

    def removerDepartamento(self):
        self.departamento = None

    def adicionarDisciplina(self, disciplina):
        if len(self.listaDisciplinas) < 5:
            self.listaDisciplinas.append(disciplina)
        else:
            print("O professor já possui o número máximo de disciplinas (5).")

    def removerDisciplina(self, disciplina):
        if disciplina in self.listaDisciplinas:
            self.listaDisciplinas.remove(disciplina)

    def listarDisciplinas(self):
        for disciplina in self.listaDisciplinas:
            print(f"Disciplina: {disciplina.nome}")

    def obterInformacoes(self):
        return f"Professor: {self.nome}, ID: {self.id}, Especialização: {self.areaEspecializacao}"