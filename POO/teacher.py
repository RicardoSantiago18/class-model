class Professor:
    def __init__(self, nome, id, especialidade):
        self.nome = nome
        self.id = id
        self.especialidade = especialidade
        self.disciplinas = []

    def adicionarDisciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)

    def removerDisciplina(self, disciplina):
        if disciplina in self.disciplinas:
            self.disciplinas.remove(disciplina)
            print(f"Disciplina {disciplina.nome} foi removida do Professor {self.nome}.")

    def listarDisciplinas(self):
        if self.disciplinas:
            for disciplina in self.disciplinas:
                print(f"- {disciplina.nome}")
        else:
            print("Nenhuma disciplina ministrada.")
